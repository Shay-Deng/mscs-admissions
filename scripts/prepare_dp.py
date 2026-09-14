"""Prepare local research data: explicit field allowlist, per-applicant outcomes, QC."""
import argparse,collections,hashlib,json,pathlib
ACADEMIC=('ug_school_category','ug_school_name','ug_major','gpa_scale','gpa','gpa_rank','graduation_year')
def prepare(rows):
    clean=[]; excluded=[]; seen=set()
    for r in rows:
        d=r['d']; a=r.get('a') or {}; p=r.get('p') or {}
        reason=None
        marker=str(d.get('notes',''))+' '+str(a.get('ug_school_name',''))
        if 'AUTOMATED' in marker.upper() and 'TEST' in marker.upper():reason='automated_test'
        if d['id'] in seen:reason='duplicate_id'
        seen.add(d['id'])
        if reason:excluded.append({'id':d['id'],'reason':reason});continue
        aid=d.get('applicant_id')
        # Missing applicant IDs must never collapse unrelated people into one group.
        key='csgrad:'+hashlib.sha256(str(aid or ('missing:'+d['id'])).encode()).hexdigest()[:20]
        clean.append({'case_id':d['id'],'applicant_key':key,'applicant_link_known':bool(aid),
          'profile':{k:a.get(k) for k in ACADEMIC},'program':{k:p.get(k) for k in ('id','school','program','tier','country')},
          'tier_axis':'program_value','result':d.get('result'),'year':d.get('academic_year'),'semester':d.get('semester'),
          'final_destination':d.get('is_final_destination'),'source_row':d.get('seatable_row_id'),
          'source':'https://csgrad.com/datapoints','source_api':'https://csgrad-positioning.capsfly7.workers.dev/api/dp'})
    groups=collections.defaultdict(list)
    for r in clean:groups[r['applicant_key']+'|'+str(r['year'])+'|'+str(r['semester'])].append(r['case_id'])
    return clean,dict(groups),excluded

def main():
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('--output',required=True);a=p.parse_args()
    clean,groups,excluded=prepare(json.loads(pathlib.Path(a.input).read_text()));out=pathlib.Path(a.output);out.mkdir(parents=True,exist_ok=True)
    for name,data in [('cases',clean),('applicant-outcomes',groups),('excluded',excluded)]:
        (out/(name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
    report={'raw_rows':len(clean)+len(excluded),'retained_rows':len(clean),'excluded_rows':len(excluded),'applicants':len({r['applicant_key'] for r in clean}),'applicant_seasons':len(groups),'multi_result_portfolios':sum(len(v)>1 for v in groups.values()),'results':dict(collections.Counter(r['result'] for r in clean)),'gpa_missing':sum(r['profile']['gpa'] is None for r in clean),'note':'Research snapshot, not a representative admissions sample. No calibrated admission probabilities. Program tiers here are CS Grad value tiers.'}
    (out/'quality.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)); print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':main()
