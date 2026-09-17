#!/usr/bin/env python3
"""Build an unpublished review edition. Never approves, deploys, or edits manuscript source.

Default: build the existing site, then apply the explicitly listed review replacements.
--baseline accepts a saved page map for local review when canonical source is unavailable.
"""
from __future__ import annotations
import argparse, hashlib, html, importlib.util, json, re, tempfile, zipfile
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
from xml.etree import ElementTree as ET
HERE = Path(__file__).resolve().parent

def read_baseline(site_root: Path, snapshot: Path | None) -> dict:
    if snapshot is not None:
        return json.loads(snapshot.read_text(encoding='utf-8'))
    spec = importlib.util.spec_from_file_location('baseline_builder', site_root / 'build.py')
    if spec is None or spec.loader is None: raise ValueError('No existing site builder')
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    with tempfile.TemporaryDirectory() as directory:
        output = Path(directory) / 'baseline'
        module.build(site_root, output)
        return {p.relative_to(output).as_posix(): {'html':p.read_text(encoding='utf-8')} for p in output.rglob('*.html')}

def build(config: dict, baseline: dict, css: str, theme_js: str, output: Path) -> dict:
    routes = config['routes']
    if len(set(routes)) != len(routes) or 'index.html' not in routes: raise ValueError('Invalid route list')
    if any(not re.fullmatch(r'(?:[a-z0-9]+(?:-[a-z0-9]+)*/)*index\.html',r) for r in routes): raise ValueError('Unsafe route')
    if output.exists() and (output.is_symlink() or not output.is_dir() or any(output.iterdir())): raise ValueError('Output must be new or empty')
    origin=config['origin']; pages={}
    esc=html.escape
    for path in routes:
        if path in config['replacements']:
            p=dict(config['replacements'][path])
        else:
            text=baseline[path]['html']
            main=re.search(r'<main\b[^>]*>.*?</main>',text,re.S)
            title=re.search(r'<h1[^>]*>(.*?)</h1>',text,re.S)
            description=re.search(r'<p[^>]*class="lede"[^>]*>(.*?)</p>',text,re.S)
            if not (main and title and description): raise ValueError('Missing page structure: '+path)
            p={'main':main.group(0),'title':html.unescape(title.group(1)),'description':html.unescape(description.group(1))}
        for old,new in config.get('text_replacements',[]):
            for key in ('main','title','description'):p[key]=p[key].replace(old,new)
        if re.search(r'<(?:script|iframe|object|embed)\b|\bon\w+\s*=',p['main'],re.I): raise ValueError('Executable markup in reading text')
        pages[path]=p
    def href(value: str, source: str, single: bool) -> str:
        if value.startswith('#'): return value
        u=urlsplit(urljoin(origin+'/'+source,value))
        if u.scheme not in ('https','http','mailto'):raise ValueError('Unsafe URL')
        if u.netloc != urlsplit(origin).netloc:return value
        target=unquote(u.path).lstrip('/')
        if not target or target.endswith('/'):target+='index.html'
        if target not in pages:raise ValueError(f'Link to excluded/missing page: {source} -> {target}')
        if single:return '#p-'+target.removesuffix('index.html').strip('/').replace('/','-') if target!='index.html' else '#p-home'
        prefix='../'*source.count('/')
        return prefix+target+('#'+u.fragment if u.fragment else '')
    def rewrite(main: str, path: str, single: bool) -> str:
        return re.sub(r'href="([^"]+)"',lambda m:'href="'+esc(href(html.unescape(m.group(1)),path,single),quote=True)+'"',main)
    controls='<fieldset id="theme-controls" class="preferences" hidden><legend>Color theme</legend><div class="theme-options">'+''.join('<label><input type="radio" name="color-theme" value="'+v+'"'+(' checked' if v=='system' else '')+'>'+t+'</label>' for v,t in [('system','System'),('light','Light'),('dark','Dark')])+'</div></fieldset><noscript><p>Colors follow your device settings. Reading and navigation work without JavaScript.</p></noscript>'
    def header(path: str, single: bool) -> str:
        nav=''.join('<a href="'+href(url,path,single)+'"'+(' aria-current="page"' if url=='/'+path.removesuffix('index.html') else '')+'>'+esc(label)+'</a>' for url,label in config['navigation'])
        return '<a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="header-row"><a class="wordmark" href="'+href('/',path,single)+'">'+esc(config['title'])+'<span>'+esc(config['tagline'])+'</span></a><nav aria-label="Main navigation">'+nav+'</nav></div>'+controls+'<p class="review-label">Review copy · Not published</p></header>'
    def footer(path: str, single: bool) -> str:
        return '<footer><p>'+esc(config['footer'])+'</p><nav class="footer-links" aria-label="Footer"><a href="'+href('/accessibility/',path,single)+'">Accessibility</a><a href="'+href('/changelog/',path,single)+'">Site updates</a><a href="'+href('/about/',path,single)+'">About</a></nav></footer>'
    def shell(title: str,description: str,body: str, extra_js: str='') -> str:
        return '<!doctype html><html lang="en" data-site="'+config['theme']+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><meta name="referrer" content="no-referrer"><meta http-equiv="Content-Security-Policy" content="default-src \'none\'; script-src \'unsafe-inline\'; style-src \'unsafe-inline\'; img-src data:; connect-src \'none\'; base-uri \'none\'; form-action \'none\'"><title>'+esc(title)+' · '+esc(config['title'])+'</title><meta name="description" content="'+esc(description,quote=True)+'"><script>'+theme_js+'</script><style>'+css+'</style></head><body>'+body+('<script>'+extra_js+'</script>' if extra_js else '')+'</body></html>'
    output.mkdir(parents=True,exist_ok=True)
    for path,p in pages.items():
        target=output/path;target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(shell(p['title'],p['description'],header(path,False)+rewrite(p['main'],path,False)+footer(path,False)),encoding='utf-8')
    # Single-file review keeps all pages present for no-JavaScript reading.
    articles=[]
    for path,p in pages.items():
        ident='p-'+path.removesuffix('index.html').strip('/').replace('/','-') if path!='index.html' else 'p-home'
        main=rewrite(p['main'],path,True)
        main=re.sub(r'^<main\b[^>]*>|</main>$','',main)
        # Prefix in-page IDs to avoid collisions when pages share the single document.
        main=re.sub(r'\bid="([^"]+)"',lambda m:'id="'+ident+'-'+m.group(1)+'"',main)
        main=re.sub(r'href="#(?!p-)([^"]+)"',lambda m:'href="#'+ident+'-'+m.group(1)+'"',main)
        articles.append('<article class="review-page" id="'+ident+'" data-title="'+esc(p['title'],quote=True)+'">'+main+'</article>')
    router="""(function(){'use strict';var pages=Array.from(document.querySelectorAll('.review-page'));function show(moveFocus){var id=location.hash.slice(1)||'p-home';var p=pages.find(function(x){return x.id===id;})||pages.find(function(x){return x.id==='p-home';});pages.forEach(function(x){x.hidden=x!==p;});document.title=p.dataset.title+' · '+document.querySelector('.wordmark').childNodes[0].textContent;document.querySelectorAll('nav a').forEach(function(a){if(a.hash==='#'+p.id)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');});if(moveFocus){var h=p.querySelector('h1');h.tabIndex=-1;h.focus();}}window.addEventListener('hashchange',function(){if(location.hash==='#main'){document.getElementById('main').focus();return;}if(location.hash.startsWith('#p-'))show(true);});show(false);}());"""
    single=shell(config['title'],pages['index.html']['description'],header('index.html',True)+'<main id="main" tabindex="-1">'+''.join(articles)+'</main>'+footer('index.html',True),router)
    # Review wrapper stays out of the website edition archive.
    review_path=output.parent/(config['site']+'-review.html');review_path.write_text(single,encoding='utf-8')
    ns='{http://www.w3.org/2005/Atom}';ET.register_namespace('',ns[1:-1]);feed=ET.Element(ns+'feed')
    for key,val in [('id',origin),('title',config['title']),('updated',config['date']+'T00:00:00Z')]:ET.SubElement(feed,ns+key).text=val
    author=ET.SubElement(feed,ns+'author');ET.SubElement(author,ns+'name').text=config['title']
    ET.SubElement(feed,ns+'link',{'href':origin+'/feed.xml','rel':'self'})
    site=ET.Element('urlset',xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
    for path,p in pages.items():
        address=origin+'/'+path.removesuffix('index.html');entry=ET.SubElement(feed,ns+'entry')
        for key,val in [('id',address),('title',p['title']),('updated',config['date']+'T00:00:00Z'),('summary',p['description'])]:ET.SubElement(entry,ns+key).text=val
        ET.SubElement(entry,ns+'link',{'href':address})
        u=ET.SubElement(site,'url');ET.SubElement(u,'loc').text=address
    (output/'feed.xml').write_bytes(ET.tostring(feed,encoding='utf-8',xml_declaration=True));(output/'sitemap.xml').write_bytes(ET.tostring(site,encoding='utf-8',xml_declaration=True))
    (output/'robots.txt').write_text('User-agent: *\nDisallow: /\n')
    manifest={'review_only':True,'base_commit':config['base_commit'],'pages':routes,'files':{p.relative_to(output).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(output.rglob('*')) if p.is_file()}}
    (output/'review-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    with zipfile.ZipFile(output/'review-edition.zip','w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(output.rglob('*')):
            if p.is_file() and p.name!='review-edition.zip':z.write(p,p.relative_to(output).as_posix())
    return manifest

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--baseline',type=Path);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    cfg=json.loads((HERE/'edition.json').read_text(encoding='utf-8'))
    baseline=read_baseline(HERE.parent,args.baseline)
    receipt=build(cfg,baseline,(HERE/'theme.css').read_text(),(HERE/'theme.js').read_text(),args.output)
    print(json.dumps({'review_only':True,'pages':len(receipt['pages']),'output':str(args.output)},indent=2))
if __name__=='__main__':main()
