#!/usr/bin/env python3
"""Validate UT-001 artifacts and trace references; semantic verdicts are manual."""
from pathlib import Path
import hashlib,json,sys
P=Path(__file__).resolve().parent
protocol=json.loads((P/'protocol.json').read_text())
assert protocol['id']=='UT-001'
assert len(protocol['conditions'])==3 and protocol['max_words']==210
if '--protocol-only' in sys.argv:
 print('UT-001 packet valid; SHA-256 '+hashlib.sha256((P/'protocol.json').read_bytes()).hexdigest());raise SystemExit
run=json.loads((P/'responses-and-audit.json').read_text())
assert run['protocol_sha256']==hashlib.sha256((P/'protocol.json').read_bytes()).hexdigest()
checks={c['id']:c for c in protocol['checks']}
refs={'fragment','clarification'}|{f['id'] for f in protocol['facts']}
expected={(c['id'],s) for c in protocol['conditions'] for s in ['initial','revised']}
assert {(r['condition'],r['stage']) for r in run['responses']}==expected
assert len(run['responses'])==6
counts=[]
for r in run['responses']:
 text=r['text'];count=len(text.split());assert count<=protocol['max_words'],(r['condition'],r['stage'],count)
 assert r['text_sha256']==hashlib.sha256(text.encode()).hexdigest()
 need={c['id'] for c in checks.values() if r['stage'] in c['applies']}
 assert {a['check'] for a in r['audit']}==need
 assert len(r['audit'])==len(need)
 for a in r['audit']:
  assert a['verdict'] in ['preserved','violated','unclear']
  assert a['reference_ids']==checks[a['check']]['reference_ids']
  assert set(a['reference_ids'])<=refs
  assert a['quotes'] and all(q and q in text for q in a['quotes']),(r['condition'],r['stage'],a['check'])
 counts.append({'condition':r['condition'],'stage':r['stage'],'words':count,'preserved':sum(a['verdict']=='preserved' for a in r['audit']),'violated':sum(a['verdict']=='violated' for a in r['audit']),'unclear':sum(a['verdict']=='unclear' for a in r['audit'])})
result={'id':'UT-001','trace_check':'pass','responses':counts,'applicable_manual_judgments':sum(len(r['audit']) for r in run['responses']),'measurement_limit':'Word counts and quote existence are computed; preservation judgments are manual and not independent. Effort and usability are not measured.'}
(P/'checked-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
