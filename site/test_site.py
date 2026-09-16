"""Offline publication tests. Temporary approvals never approve the actual site."""
from __future__ import annotations
import copy
import importlib.util
import json
import shutil
import tempfile
import unittest
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
from xml.etree import ElementTree as ET

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('seed_builder', HERE / 'build.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids, self.tags, self.meta = [], set(), [], {}
        self.headings = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if tag == 'h1': self.headings += 1
        if 'id' in attrs: self.ids.add(attrs['id'])
        if tag in ('a','link') and 'href' in attrs: self.links.append(attrs['href'])
        if tag == 'meta': self.meta[attrs.get('name')] = attrs.get('content')

class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'source'
        self.root.mkdir()
        for name in ('build.py','style.css','content.json'):
            shutil.copy2(HERE / name, self.root / name)
        self.data = json.loads((self.root/'content.json').read_text())
    def build(self, release=False):
        output = Path(self.temp.name) / 'output'
        return output, builder.build(self.root, output, release)
    def write(self):
        (self.root/'content.json').write_text(json.dumps(self.data))
    def test_preview_pages_have_structure_and_no_scripts(self):
        output, result = self.build()
        self.assertEqual(result['html_pages'], len(self.data['pages']))
        for p in output.rglob('*.html'):
            doc = PageParser(); doc.feed(p.read_text())
            self.assertEqual(doc.headings, 1)
            self.assertIn('main', doc.ids)
            self.assertNotIn('script', doc.tags)
            self.assertEqual(doc.meta['robots'], 'noindex,nofollow')
            self.assertTrue(doc.meta['description'])
    def test_every_local_link_and_fragment_resolves(self):
        output,_ = self.build()
        for p in output.rglob('*.html'):
            doc=PageParser(); doc.feed(p.read_text())
            for href in doc.links:
                url=urlparse(href)
                if url.scheme or url.netloc: continue
                target=(p.parent/unquote(url.path)).resolve() if url.path else p.resolve()
                self.assertTrue(target.is_relative_to(output.resolve()))
                self.assertTrue(target.is_file(), f'{p.name}: {href}')
                if url.fragment:
                    target_doc=PageParser(); target_doc.feed(target.read_text())
                    self.assertIn(url.fragment,target_doc.ids)
    def test_feed_and_sitemap_are_parseable_and_complete(self):
        output,_=self.build()
        feed=ET.parse(output/'feed.xml')
        self.assertEqual(len(feed.findall('{http://www.w3.org/2005/Atom}entry')),len(self.data['pages']))
        self.assertEqual(len(ET.parse(output/'sitemap.xml').getroot()),len(self.data['pages']))
    def test_archive_is_self_contained_and_excludes_source(self):
        output,result=self.build()
        with zipfile.ZipFile(output/'seed-archive.zip') as z:
            names=set(z.namelist())
            self.assertIn('index.html',names)
            self.assertIn('build-manifest.json',names)
            self.assertTrue(set(result['files']).issubset(names))
            for private_name in ('content.json','build.py','approval.json','EDITORIAL-NOTES.md'):
                self.assertNotIn(private_name,names)
    def test_missing_approval_blocks_release(self):
        with self.assertRaisesRegex(ValueError,'Release blocked'): self.build(True)
    def test_exact_approval_allows_release(self):
        approval={'source_sha256':builder.source_digest(self.root),'approved_by':'test-fixture-only','approved_at':'2026-09-16'}
        (self.root/'approval.json').write_text(json.dumps(approval))
        output,result=self.build(True)
        self.assertEqual(result['build_mode'],'release')
        self.assertNotIn('noindex',(output/'index.html').read_text())
    def test_source_change_invalidates_approval(self):
        approval={'source_sha256':builder.source_digest(self.root),'approved_by':'test-fixture-only','approved_at':'2026-09-16'}
        (self.root/'approval.json').write_text(json.dumps(approval))
        self.data['pages'][0]['title'] += ' revised'
        self.write()
        with self.assertRaisesRegex(ValueError,'Release blocked'): self.build(True)
    def test_unsafe_or_duplicate_slug_is_rejected(self):
        for bad in ('../secret/','/absolute/','a//b/',''):
            data=copy.deepcopy(self.data); data['pages'][1]['slug']=bad
            with self.assertRaises(ValueError): builder.validate(data)
    def test_external_javascript_url_is_rejected(self):
        self.data['nav'][0]['url']='javascript:alert(1)'
        with self.assertRaises(ValueError): builder.validate(self.data)
    def test_unknown_internal_target_is_rejected(self):
        self.data['nav'][0]['url']='/does-not-exist/'
        with self.assertRaises(ValueError): builder.validate(self.data)
    def test_existing_output_is_not_overwritten(self):
        output,_=self.build()
        marker=output/'reader-note.txt'; marker.write_text('keep me')
        with self.assertRaisesRegex(ValueError,'empty output'): builder.build(self.root,output)
        self.assertEqual(marker.read_text(),'keep me')
    def test_text_is_escaped_and_graph_is_consistent(self):
        self.data['pages'][0]['sections'][0]['paragraphs'].append('<script>secret</script>')
        self.write(); output,_=self.build()
        text=(output/'index.html').read_text()
        self.assertIn('&lt;script&gt;secret&lt;/script&gt;',text)
        self.assertNotIn('<script>',text)
        graph=json.loads((output/'project-map.json').read_text())
        ids={n['id'] for n in graph['projects']}
        for edge in graph['relationships']:
            self.assertIn(edge['from'],ids); self.assertIn(edge['to'],ids)
    def test_export_contains_no_private_repository_addresses(self):
        output,_=self.build()
        for path in output.rglob('*'):
            if path.is_file() and path.suffix in ('.html','.json','.xml','.txt'):
                text=path.read_text()
                for forbidden in ('github.com/Root-Sequence/wiki-private','github.com/Root-Sequence/coherent-world','INTEGRATION-QUEUE.md'):
                    self.assertNotIn(forbidden,text)
    def test_homepage_explains_project_before_metadata(self):
        output,_=self.build(); text=(output/'index.html').read_text()
        self.assertIn('<h1>Root Sequence</h1>',text)
        self.assertIn('collection of research, essays, and projects',text)
        self.assertIn('Rae Lovejoy',text)
        self.assertGreater(text.index('class="page-details"'),text.index('Browse the guides'))
    def test_plain_navigation_and_native_details(self):
        self.assertEqual([n['label'] for n in self.data['nav']],['Start here','Guides','Projects','About'])
        output,_=self.build()
        for path in output.rglob('*.html'):
            self.assertIn('<summary>About this page</summary>',path.read_text())
    def test_site_copy_avoids_selected_stock_patterns(self):
        import re
        output,_=self.build()
        # House-style regression only. This does not detect authorship or verify claims.
        for path in output.rglob('*.html'):
            text=re.sub('<[^>]+>',' ',path.read_text()).lower()
            for phrase in ('—','at its core','delve into','in today’s world','seamless','living systems commons','canonical identity','possibility space'):
                self.assertNotIn(phrase,text,str(path))
    def test_copy_rules_are_not_exported(self):
        output,_=self.build()
        self.assertFalse((output/'AGENTS.md').exists())
        self.assertFalse((output/'COPY-REVIEW.md').exists())

if __name__=='__main__':
    unittest.main(verbosity=2)
