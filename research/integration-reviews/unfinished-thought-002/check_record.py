#!/usr/bin/env python3
"""UT-002 trace integrity, not an independent semantic scorer."""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
protocol=json.loads((P/'protocol.json').read_text());assert protocol['id']=='UT-002'
run=json.loads((P/'run.json').read_text());assert run['protocol_sha256']==hashlib.sha256((P/'protocol.json').read_bytes()).hexdigest()
by_stage={};summary=[]
for stage in ['initial','revised']:
 data=json.loads((P/(stage+'-responses.json')).read_text());by_stage[stage]={r['id']:r for r in data['responses']}
 assert len(data['responses'])==3 and len(by_stage[stage])==3
 for r in data['responses']:
  assert hashlib.sha256(r['text'].encode()).hexdigest()==r['text_sha256']
  assert len(r['text'].split())==r['words']<=protocol['max_words']
 evaluation=json.loads((P/(stage+'-evaluation.json')).read_text());assert {r['id'] for r in evaluation['responses']}==set(by_stage[stage])
 need={c['id'] for c in protocol['rubric'] if stage=='revised' or c.get('stage')!='revised'}
 for r in evaluation['responses']:
  assert len(r['audit'])==len(need) and {a['check'] for a in r['audit']}==need
  for a in r['audit']:
   assert a['verdict'] in protocol['verdicts'] and a['reason']
   assert a['quotes'] or a['verdict'] in ['not_addressed','unclear']
   assert all(q and q in by_stage[stage][r['id']]['text'] for q in a['quotes']),(stage,r['id'],a['check'])
  summary.append({'stage':stage,'id':r['id'],'method':by_stage[stage][r['id']]['method'],'words':by_stage[stage][r['id']]['words'],'ratings':{v:sum(a['verdict']==v for a in r['audit']) for v in protocol['verdicts']},'interpretation':'Evaluator verdicts preserved; no coordinator rescore.'})
assert set(by_stage['initial'])==set(by_stage['revised'])
events={e['event']:i for i,e in enumerate(run['events'])}
for a,b in [('protocol_committed_before_generation','initial_responses_locked_before_clarification_release'),('initial_responses_locked_before_clarification_release','initial_evaluation_locked'),('initial_evaluation_locked','initial_lock_committed'),('initial_lock_committed','clarification_released'),('clarification_released','revised_responses_locked'),('revised_responses_locked','revised_evaluation_locked')]:assert events[a]<events[b],(a,b)
# The stage-one packets must not include any field carrying the future clarification or previous output/evaluation.
for p in (P/'exposure-packets').glob('producer-*.json'):
 x=json.loads(p.read_text());assert set(x)=={'case_fragment','facts','task','format_instruction','return_format'}
 assert protocol['sealed_clarification'] not in p.read_text()
x=json.loads((P/'initial-evaluation-input.json').read_text());assert set(x)=={'stage','fragment','facts','rubric','verdicts','responses'}
assert protocol['sealed_clarification'] not in (P/'initial-evaluation-input.json').read_text()
result={'id':'UT-002','trace_check':'pass','responses':summary,'measurement_limit':'Fresh contexts provide prompt separation, not independent model families or verified security isolation. Semantic scores are evaluator judgments. Human effort and causal layout effects were not measured.'}
(P/'checked-results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
