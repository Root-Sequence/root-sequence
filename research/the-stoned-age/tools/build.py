#!/usr/bin/env python3
"""Build static reader editions. Stdlib for HTML/SVG; optional reportlab for PDFs."""
from pathlib import Path
import json, re, html, math
P=Path(__file__).resolve().parents[1]
S=json.loads((P/'research/sources.json').read_text())
INK='#182d30'; PAPER='#f6f0df'; ORANGE='#bd461f'; GREEN='#326b5c'
def scene(kind):
 a=[]
 def t(x,y,s,size=20,col=INK): a.append(('text',x,y,s,size,col))
 def l(x,y,u,v,col=INK): a.append(('line',x,y,u,v,col))
 def c(x,y,r,col=INK): a.append(('circle',x,y,r,col))
 def box(x,y,w,h,col=INK): a.append(('rect',x,y,w,h,col))
 if kind in ('cover','orbit'):
  for r in [45,80,115,150]: c(400,170,r,GREEN)
  for j in range(14):
   q=j*math.pi*2/14;c(400+150*math.cos(q),170+150*math.sin(q),4,ORANGE)
  t(381,194,'?',76,ORANGE)
  t(32,55,'WONDER',18);t(32,290,'A QUESTION IS AN OPENING.',16)
 elif kind=='steps':
  for i,(x,y) in enumerate([(35,40),(225,100),(415,160),(605,220)]):
   box(x,y,160,70,GREEN);t(x+12,y+28,['EXPERIENCE','INTERPRETATION','EVIDENCE','AUTHORITY'][i],14)
   t(x+12,y+52,['What happened?','What does it mean?','What supports it?','Who may decide?'][i],12)
   if i<3:l(x+160,y+35,x+190,y+95,ORANGE)
  t(35,325,'THE CONNECTIONS REQUIRE JUSTIFICATION.',18)
 elif kind=='windows':
  for i,(name,sub) in enumerate([('ARAD','Shrine residues'),('PAMIRS','Funerary braziers'),('SOUTH AMERICA','Ritual bundle'),('MENORCA','Human hair')]):
   x=25+i*195;box(x,45,175,205,GREEN);c(x+88,105,32,ORANGE);t(x+10,180,name,15);t(x+10,210,sub,13)
  t(25,300,'FOUR WINDOWS. NO UNIVERSAL ORIGIN STORY.',18)
 elif kind=='ladder':
  for i,s in enumerate(['EXPOSURE','EFFECTS','TRANSMISSION','BETTER EXPLANATION']):
   y=285-i*70;l(90,y,730,y,GREEN);t(110,y-12,s,19);t(750,y,'?',27,ORANGE)
  l(90,35,90,310);l(730,35,730,310)
 elif kind=='split':
  for x,title,sub in [(35,'IDEAS ARRIVING','Novelty / significance'),(435,'IDEAS BEING CHECKED','Accuracy / usefulness')]:
   box(x,35,330,250,GREEN);t(x+20,75,title,18);t(x+20,108,sub,16)
   for y in range(145,265,30): l(x+20,y,x+300,y,GREEN)
  t(35,330,'KEEP BOTH NOTEBOOKS.',20,ORANGE)
 elif kind in ('network','branch'):
  words=['EXPERIENCE','REPORT','CONTEXT','AUDIENCE','REVISION','MEMORY']
  pts=[(110,90),(400,50),(685,100),(650,270),(365,280),(110,250)]
  for i,(x,y) in enumerate(pts):
   u,v=pts[(i+1)%6];l(x,y,u,v,GREEN);l(x,y,400,165,GREEN)
  for i,(x,y) in enumerate(pts):c(x,y,16,ORANGE);t(x-50,y+40,words[i],13)
  c(400,165,37,ORANGE);t(391,175,'?',30)
 elif kind=='boundary':
  c(280,175,130,GREEN);c(520,175,130,ORANGE);t(185,165,'EXPERIENCE',20);t(470,195,'CONSENT',20);t(30,330,'SIGNIFICANCE DOES NOT CANCEL REFUSAL.',18)
 elif kind=='mirror':
  for i in range(4):
   x=25+i*195;box(x,45+i*15,175,190,GREEN);t(x+20,135+i*15,'ONE CLAIM',17)
  t(25,320,'FOUR REFLECTIONS ARE NOT FOUR WITNESSES.',18,ORANGE)
 return a
descriptions={'cover':'Concentric orbits around a question mark: wonder opens inquiry','orbit':'Concentric orbits around a question mark','steps':'Four separate questions: experience, interpretation, evidence and authority','windows':'Four archaeological evidence types: shrine residues, braziers, ritual bundle and hair','branch':'A network linking experience, report, context, audience, revision and memory','network':'A network linking experience, report, context, audience, revision and memory','ladder':'An evidential ladder: exposure, effects, transmission and a better explanation; each step remains a question','split':'Two notebooks separate arriving ideas from checked ideas','boundary':'Overlapping circles distinguish experience and consent','mirror':'Four repetitions of one claim do not make four independent witnesses'}
arts=['cover','orbit','steps','windows','branch','ladder','split','network','boundary','mirror']
for kind in arts:
 out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 360" role="img" aria-labelledby="title"><title id="title">{descriptions[kind]}</title><rect width="800" height="360" fill="{PAPER}"/>']
 for z in scene(kind):
  if z[0]=='text': _,x,y,s,size,col=z;out.append(f'<text x="{x}" y="{y}" fill="{col}" font-family="sans-serif" font-size="{size}">{html.escape(s)}</text>')
  elif z[0]=='line': _,x,y,u,v,col=z;out.append(f'<path d="M{x} {y} L{u} {v}" fill="none" stroke="{col}" stroke-width="2"/>')
  elif z[0]=='circle': _,x,y,r,col=z;out.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{col}" stroke-width="2"/>')
  else: _,x,y,w,h,col=z;out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{col}" stroke-width="2"/>')
 (P/f'assets/{kind}.svg').write_text(''.join(out)+'</svg>')
css='''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f6f0df;color:#182d30;font:19px/1.7 Georgia,serif}a{color:#245c50;text-underline-offset:4px}a:focus-visible,button:focus-visible,summary:focus-visible{outline:3px solid #bd461f;outline-offset:5px}header,main,footer{max-width:1080px;margin:auto;padding:32px}nav{display:flex;flex-wrap:wrap;gap:12px 25px;font:15px/1.5 system-ui}h1{font-size:clamp(54px,10vw,112px);line-height:.95;letter-spacing:-.055em;max-width:850px;margin:55px 0 30px}h2{font-size:clamp(28px,4vw,44px);line-height:1.18;letter-spacing:-.025em;margin-top:65px}h3{font-size:23px}p,li{max-width:750px}.eyebrow{font:13px/1.4 system-ui;text-transform:uppercase;letter-spacing:.14em;color:#93401f}.deck{font-size:27px;max-width:760px}img{width:100%;height:auto;display:block;margin:35px 0}figure{margin:0}figcaption,.meta{font:14px/1.5 system-ui;color:#435955}.rule{border-top:2px solid #182d30;margin-top:35px;padding-top:25px}.skip{position:absolute;left:-9999px}.skip:focus{left:20px;top:10px;background:white;padding:10px}.editions{display:grid;grid-template-columns:1fr 1fr;gap:25px}.editions a{display:block;border-top:2px solid;padding:18px 0}.refs{font:15px/1.6 system-ui}.refs li{margin-bottom:15px;overflow-wrap:anywhere}.chapter{break-before:page;border-top:1px solid #b6bdac;padding-top:20px;margin-top:40px}.slide{min-height:85vh;border-top:2px solid #326b5c;padding:30px 0}.slide h2{margin-top:15px}.slide img{max-width:800px}details{font:16px/1.6 system-ui;margin:20px 0}table{border-collapse:collapse;font:15px/1.5 system-ui}td,th{padding:10px;border:1px solid #b6bdac;text-align:left}blockquote{border-left:4px solid #bd461f;padding-left:20px}code{font-size:.85em}@media(max-width:600px){header,main,footer{padding:22px}body{font-size:18px}.editions{grid-template-columns:1fr}nav{gap:10px 15px}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}@media print{nav,.skip{display:none}body{background:white;font-size:11pt}header,main,footer{padding:0}h1{font-size:45pt}h2{font-size:24pt}a{color:inherit}img{max-height:65mm}.slide{page-break-after:always;min-height:0}.slide details{display:none}}'''
(P/'assets/style.css').write_text(css)
def refhtml(prefix='../'):
 return '<ol class="refs">'+''.join(f'<li id="{s["id"]}"><b>{s["id"]}</b> · {html.escape(s["authors"])} ({s["year"]}). <a href="{s["url"]}">{html.escape(s["title"])}</a>. {html.escape(s["venue"])}</li>' for s in S)+'</ol>'
def inline(t):
 t=html.escape(t)
 t=re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',r'<img alt="\1" src="\2">',t)
 t=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',t)
 t=re.sub(r'\[\^(S\d+)\]',r'<sup><a href="#\1">\1</a></sup>',t)
 t=t.replace('[S01–S04]','[S01, S02, S03, S04]')
 t=re.sub(r'\[(S\d+(?:, S\d+)*)\]',lambda m:'<span class="meta">['+', '.join(f'<a href="#'+x+'">'+x+'</a>' for x in m[1].split(', '))+']</span>',t)
 t=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',t)
 t=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<em>\1</em>',t)
 return t
# Deliberately small renderer for the controlled source format; Markdown remains canonical.
def md(t):
 out=[]
 for b in t.split('\n\n'):
  if b.startswith('[^'):continue
  if b.startswith('#'):
   first,*rest=b.split('\n');n=len(first)-len(first.lstrip('#'));text=first[n:].strip();anchor=re.sub('[^a-z0-9]+','-',text.lower()).strip('-');out.append(f'<h{n} id="{anchor}">{inline(text)}</h{n}>')
   if rest:out.append('<p>'+inline(' '.join(rest))+'</p>')
  elif b.startswith('- '):out.append('<ul>'+''.join('<li>'+inline(x[2:])+'</li>' for x in b.splitlines())+'</ul>')
  else:out.append('<p>'+inline(b).replace('\n',' ')+'</p>')
 return '\n'.join(out)
def page(title,body,sub=True):
 pre='../' if sub else ''
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="A sourced inquiry into altered states, curiosity, meaning and authority."><title>{title} — The Stoned Age</title><link rel="stylesheet" href="{pre}assets/style.css"></head><body><a class="skip" href="#main">Skip to content</a><header><nav aria-label="Editions"><a href="{pre}index.html">The project</a><a href="{pre}essay/index.html">Web essay</a><a href="{pre}booklet/index.html">Booklet</a><a href="{pre}paper/index.html">Paper</a><a href="{pre}talk/index.html">Talk</a><a href="{pre}research/sources.html">Sources</a><a href="{pre}research/appraisal.html">Evidence notes</a></nav></header><main id="main">{body}</main><footer class="meta rule">Root Sequence · v0.1.2 · 24 October 2026 · AI-assisted draft, author and disciplinary review pending.<br>Original conceptual illustrations. No historical reconstructions. No tracking, external fonts or runtime dependencies.</footer></body></html>'''
for path,title in [('essay/essay.md','Illustrated essay'),('paper/manuscript.md','Living paper')]:
 txt=(P/path).read_text();body=md(txt.split('## References')[0])+'<h2>References</h2>'+refhtml()
 (P/Path(path).parent/'index.html').write_text(page(title,body))
book=json.loads((P/'booklet/book.json').read_text())
body='<p class="eyebrow">Illustrated reader edition</p><h1>The Stoned Age</h1><p><a href="the-stoned-age.pdf">Download the 16-page booklet PDF</a> · <a href="book.md">Markdown source</a></p>'
for i,b in enumerate(book):
 body+=f'<section class="chapter"><p class="eyebrow">{i+1:02d}</p><h2>{b["title"]}</h2><p class="deck">{b["deck"]}</p><img src="../assets/{b["art"]}.svg" alt="{descriptions[b["art"]]}">{md(b["text"])}</section>'
body+='<h2>References</h2>'+refhtml();(P/'booklet/index.html').write_text(page('Booklet',body))
slides=json.loads((P/'talk/slides.json').read_text());body='<h1>The Stoned Age</h1><p>25-minute talk · <a href="the-stoned-age-talk.pdf">Slide PDF</a> · <a href="outline.md">Speaker outline</a></p>'
for i,s in enumerate(slides):
 body+=f'<section class="slide" id="slide-{i+1}"><p class="eyebrow">{i+1:02d} / 12 · {s["time"]}</p><h2>{s["title"]}</h2><p class="deck">{s["onscreen"]}</p><img src="../assets/{s["art"]}.svg" alt="{descriptions[s["art"]]}"><p class="meta">{inline("["+s["refs"]+"]") if s["refs"] else "Editorial framing"}</p><details><summary>Speaker notes</summary><p>{s["notes"]}</p></details></section>'
body+='<h2>References</h2>'+refhtml();(P/'talk/index.html').write_text(page('Talk',body))

(P/'booklet/book.md').write_text('# The Stoned Age — reader edition\n\n'+'\n\n---\n\n'.join('## '+x['title']+'\n\n*'+x['deck']+'*\n\n![Conceptual illustration: '+x['art']+'](../assets/'+x['art']+'.svg)\n\n'+x['text'] for x in book)+'\n\n## References\n\nSee the [shared source register](../research/sources.md) and [appraisal](../research/appraisal.md).\n')
(P/'talk/outline.md').write_text('# The Stoned Age — 25-minute talk\n\nv0.1.2 · 24 October 2026. 21 minutes speaking plus 4 minutes discussion. AI-assisted draft; review pending.\n\n'+'\n\n'.join(f"## {i+1}. {x['title']} ({x['time']})\n\n**On screen:** {x['onscreen']}\n\n**Speaker notes:** {x['notes']}\n\n**Visual:** [Conceptual illustration](../assets/{x['art']}.svg).\n\n**Sources:** {x['refs'] or 'Editorial framing'}" for i,x in enumerate(slides))+'\n\nSee the [source register](../research/sources.md) and [appraisal](../research/appraisal.md).\n')

(P/'research/appraisal.html').write_text(page('Source appraisal',md((P/'research/appraisal.md').read_text())))
(P/'research/sources.html').write_text(page('Sources','<h1>Sources & limits</h1><p><a href="appraisal.html">Read the source-by-source appraisal</a></p><p>16 source records. See <a href="sources.md">inspection notes</a>, <a href="claims.csv">claims ledger</a> and <a href="methods.md">method and research agenda</a>.</p>'+refhtml()))
(P/'index.html').write_text(page('Project suite','''<p class="eyebrow">Root Sequence / a living inquiry / v0.1.2</p><h1>The<br>Stoned Age</h1><p class="deck">Altered States, Human Curiosity, and the Long History of Making Meaning</p><img src="assets/cover.svg" alt="Concentric orbits around a question mark: wonder begins an inquiry"><p>What happens after somebody says, “I have figured it all out”?</p><p>A playful, intellectually serious inquiry into changed experience, human origins, religion, shared stories and AI. The companion provocation is <em>How Drugs Explain the Universe</em>. The evidence has a more careful story to tell.</p><div class="editions"><a href="essay/index.html"><strong>01 / The illustrated essay</strong><br>A doorway into the argument.</a><a href="booklet/index.html"><strong>02 / The small book</strong><br>16 illustrated pages, plus an accessible HTML edition.</a><a href="paper/index.html"><strong>03 / The living paper</strong><br>The argument, sources, hypotheses and limits.</a><a href="talk/index.html"><strong>04 / The talk</strong><br>12 slides and a 25-minute speaker outline.</a></div><section class="rule"><h2>Wonder is welcome.<br>Claims remain accountable.</h2><p>This is an AI-assisted first edition, not a peer-reviewed release. Root Sequence coordinates inquiry; it does not claim specialist authority. Each edition draws from a shared source register.</p><p><a href="research/sources.html">Inspect the sources</a> · <a href="research/claims.csv">Download the claims ledger</a> · <a href="research/methods.md">Method and next research steps</a> · <a href="README.md">Project record and exact placement</a></p></section>''',False))
# Optional PDFs. All content is also available in semantic HTML.
try:
 from reportlab.pdfgen import canvas
 from reportlab.platypus import Paragraph
 from reportlab.lib.styles import ParagraphStyle
 from reportlab.lib.colors import HexColor
except ImportError:
 print('HTML and SVG built. Install reportlab to build PDFs.');raise SystemExit

def drawart(cv,kind,x,y,w):
 cv.saveState();cv.translate(x,y);cv.scale(w/800,w/800)
 for z in scene(kind):
  if z[0]=='text':
   _,xx,yy,s,size,col=z;cv.setFillColor(HexColor(col));cv.setFont('Helvetica',size);cv.drawString(xx,360-yy,s)
  elif z[0]=='line':
   _,xx,yy,u,v,col=z;cv.setStrokeColor(HexColor(col));cv.setLineWidth(2);cv.line(xx,360-yy,u,360-v)
  elif z[0]=='circle':
   _,xx,yy,r,col=z;cv.setStrokeColor(HexColor(col));cv.circle(xx,360-yy,r,stroke=1,fill=0)
  else:
   _,xx,yy,ww,hh,col=z;cv.setStrokeColor(HexColor(col));cv.rect(xx,360-yy-hh,ww,hh,stroke=1,fill=0)
 cv.restoreState()
def para(cv,text,x,y,w,size=12,leading=None,font='Times-Roman',color=INK):
 st=ParagraphStyle('p',fontName=font,fontSize=size,leading=leading or size*1.4,textColor=HexColor(color),spaceAfter=8)
 text=html.escape(text).replace('\n','<br/>')
 obj=Paragraph(text,st);_,h=obj.wrap(w,10000);obj.drawOn(cv,x,y-h);return y-h-12

def frame(cv,w,h,num,label):
 cv.setFillColor(HexColor(PAPER));cv.rect(0,0,w,h,fill=1,stroke=0)
 cv.setFillColor(HexColor(INK));cv.setFont('Helvetica',8);cv.drawString(35,22,label+' / v0.1.2 / review pending');cv.drawRightString(w-35,22,str(num))
cv=canvas.Canvas(str(P/'booklet/the-stoned-age.pdf'),pagesize=(420,595),invariant=1);cv.setTitle('The Stoned Age — illustrated reader edition');cv.setAuthor('Root Sequence; AI-assisted draft')
for i,b in enumerate(book):
 frame(cv,420,595,i+1,'THE STONED AGE')
 y=para(cv,b['title'],35,554,350,27,30,'Helvetica-Bold')
 y=para(cv,b['deck'],35,y,350,12,16,'Helvetica',ORANGE)
 drawart(cv,b['art'],35,y-157,350);y-=173
 for p in b['text'].split('\n\n'):y=para(cv,p,35,y,350,10.8,14.4)
 if y<35:raise ValueError(f'Book page {i+1} overflow {y}')
 cv.showPage()
for j in range(4):
 frame(cv,420,595,13+j,'THE STONED AGE / SOURCES')
 y=para(cv,'Sources & reading',35,554,350,26,30,'Helvetica-Bold')
 y=para(cv,'Source IDs in the text connect here. Full access notes and limitations are in the shared source register.',35,y,350,10.5,14)
 for s in S[j*4:j*4+4]:
  label=f"{s['id']} · {s['authors']} ({s['year']}). {s['title']}. {s['venue']}."
  y=para(cv,label,35,y,350,10.5,14)
  url='https://doi.org/'+s['doi'] if s['doi'] else s['url']
  top=y;y=para(cv,url,35,y,350,8.5,11,'Helvetica',GREEN);cv.linkURL(url,(35,y,385,top),relative=0)
 if y<35:raise ValueError('References overflow')
 cv.showPage()
cv.save()
cv=canvas.Canvas(str(P/'talk/the-stoned-age-talk.pdf'),pagesize=(960,540),invariant=1);cv.setTitle('The Stoned Age — talk');cv.setAuthor('Root Sequence; AI-assisted draft')
for i,s in enumerate(slides):
 frame(cv,960,540,i+1,'THE STONED AGE / TALK')
 y=para(cv,s['title'],45,487,870,38,43,'Helvetica-Bold')
 para(cv,s['onscreen'],45,y,870,22,28)
 drawart(cv,s['art'],90,60,730)
 cv.setFillColor(HexColor(INK));cv.setFont('Helvetica',10);cv.drawString(45,42,('Sources: '+s['refs'] if s['refs'] else 'Editorial framing / proposed question')+' | Source URLs: accompanying outline and register')
 cv.showPage()
cv.save()
print('Built HTML, 10 SVG illustrations, 16-page booklet PDF, 12-slide PDF.')
