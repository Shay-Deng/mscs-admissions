"""Fetch public CS Grad rows, with bounded pagination and provenance. Raw output stays local."""
import argparse, datetime, hashlib, json, pathlib, time, subprocess
BASE = 'https://csgrad-positioning.capsfly7.workers.dev/api/dp'
def main():
    p=argparse.ArgumentParser(); p.add_argument('--output', required=True); a=p.parse_args()
    out=pathlib.Path(a.output); out.mkdir(parents=True,exist_ok=True)
    rows=[]; seen=set(); totals=[]; pages=[]; offset=0
    for page in range(100):
        url=f'{BASE}?limit=200&offset={offset}'
        raw=subprocess.check_output(['curl','--silent','--show-error','--fail','--location','--max-time','40','--user-agent','mscs-admissions-research/0.1',url])
        payload=json.loads(raw); batch=payload['rows']; totals.append(payload['total'])
        (out/f'page-{page:03}.json').write_bytes(raw)
        pages.append({'url':url,'sha256':hashlib.sha256(raw).hexdigest(),'rows':len(batch)})
        if not batch and offset<totals[-1]: raise RuntimeError('Unexpected empty page')
        for r in batch:
            rid=r['d']['id']
            if rid in seen: raise RuntimeError('Pagination overlap: retry a fresh snapshot')
            seen.add(rid);rows.append(r)
        offset+=len(batch)
        if offset>=totals[-1]:break
        time.sleep(0.7)
    else: raise RuntimeError('Pagination bound reached')
    if len(set(totals))!=1 or len(rows)!=totals[-1]:raise RuntimeError('Counts changed during fetch')
    (out/'rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
    manifest={'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'total':len(rows),'pages':pages,'scope':'public endpoint; no authentication; raw data local only'}
    (out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    print(json.dumps({'total':len(rows),'pages':len(pages)}))
if __name__=='__main__':main()
