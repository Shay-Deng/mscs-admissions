"""Filter comparable cases and show each person's entire same-season portfolio."""
import argparse,json,pathlib

def select_portfolios(rows,school='',category='',scale='',gpa_min=None,gpa_max=None,year=None):
    def match(r):
        a=r['profile']; g=a.get('gpa')
        if school and school.casefold() not in str(r['program']['school']).casefold():return False
        if category and a.get('ug_school_category')!=category:return False
        if scale and str(a.get('gpa_scale'))!=scale:return False
        if year is not None and r['year']!=year:return False
        if gpa_min is not None or gpa_max is not None:
            if not scale:raise ValueError('GPA filtering requires explicit original scale')
            try:g=float(g)
            except (TypeError,ValueError):return False
            if gpa_min is not None and g<gpa_min:return False
            if gpa_max is not None and g>gpa_max:return False
        return True
    keys={(r['applicant_key'],r['year'],r['semester']) for r in rows if match(r)}
    return [{'applicant_key':k[0],'year':k[1],'semester':k[2], 'outcomes':[r for r in rows if (r['applicant_key'],r['year'],r['semester'])==k]} for k in sorted(keys,key=str)]

def main():
    p=argparse.ArgumentParser();p.add_argument('cases');p.add_argument('--school',default='');p.add_argument('--category',default='');p.add_argument('--scale',default='');p.add_argument('--gpa-min',type=float);p.add_argument('--gpa-max',type=float);p.add_argument('--year',type=int);a=p.parse_args()
    if (a.gpa_min is not None or a.gpa_max is not None) and not a.scale:p.error('GPA filtering requires --scale')
    rows=json.loads(pathlib.Path(a.cases).read_text());result=select_portfolios(rows,a.school,a.category,a.scale,a.gpa_min,a.gpa_max,a.year)
    print(json.dumps({'matched_portfolios':len(result),'portfolios':result},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
