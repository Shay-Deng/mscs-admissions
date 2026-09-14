"""Search the local source corpus, or read a full document by its stable ID."""
import argparse,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
def read_document(d,corpus):
    return corpus[d['document_id']] if 'document_id' in d else (ROOT/d['file']).read_text()
def main():
    p=argparse.ArgumentParser();p.add_argument('query',nargs='?');p.add_argument('--document');p.add_argument('--limit',type=int,default=8);a=p.parse_args()
    if not a.query and not a.document:p.error('Provide a query or --document ID')
    data=json.loads((ROOT/'references/sources.json').read_text());corpus=json.loads((ROOT/'references/corpus.json').read_text())
    if a.document:
        for d in data['documents']:
            if d.get('document_id',d.get('file'))==a.document:
                print(json.dumps({**d,'text':read_document(d,corpus)},ensure_ascii=False));return
        p.error('Unknown document ID')
    terms=a.query.casefold().split();found=[]
    for d in data['documents']:
        body=read_document(d,corpus);low=body.casefold();identity=d.get('document_id',d.get('file',''))
        if all(t in low or t in identity.casefold() for t in terms):
            score=sum(5*(t in identity.casefold())+low.count(t) for t in terms);found.append((score,d,body))
    for _,d,body in sorted(found,key=lambda r:r[0],reverse=True)[:a.limit]:
        matches=[{'line':i+1,'text':line[:800]} for i,line in enumerate(body.splitlines()) if any(t in line.casefold() for t in terms)]
        print(json.dumps({**d,'document_id':d.get('document_id',d.get('file')),'matches':matches[:12]},ensure_ascii=False))
if __name__=='__main__':main()
