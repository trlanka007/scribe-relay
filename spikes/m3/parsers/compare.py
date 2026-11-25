"""Disposable M3 parser comparison. Generated trusted DOCX only; never use for untrusted files."""
import json, io, zipfile, hashlib, platform
from importlib.metadata import version
from pathlib import Path
from xml.etree import ElementTree as ET
import mistune
from markdown_it import MarkdownIt
from docx import Document
from docx.shared import Inches
from PIL import Image

def make_docx():
    d=Document(); d.add_heading('Synthetic title',0); d.add_heading('Heading',2)
    p=d.add_paragraph('Unicode: café, తెలుగు, 日本語, αβγ. '); p.add_run('Bold').bold=True; p.add_run('italic').italic=True
    d.add_paragraph('First',style='List Number'); d.add_paragraph('Second',style='List Number')
    t=d.add_table(rows=2,cols=2)
    for row,values in zip(t.rows,[('Feature','Value'),('Alpha','One')]):
        for cell,value in zip(row.cells,values): cell.text=value
    im=io.BytesIO(); Image.new('RGB',(64,32),'blue').save(im,format='PNG'); im.seek(0)
    d.add_paragraph('Before image'); d.add_picture(im,width=Inches(1)); d.add_paragraph('After image')
    out=io.BytesIO(); d.save(out); return out.getvalue()

def docx_probe(data):
    # Only generated trusted bytes; not a general untrusted-file parser.
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        root=ET.fromstring(z.read('word/document.xml')); ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
        body=root.find('w:body',ns)
        xml_blocks=[x.tag.rsplit('}',1)[-1] for x in body]
        xml_text=[x.text for x in root.findall('.//w:t',ns)]
        media=[x for x in z.namelist() if x.startswith('word/media/')]
        drawings=len(root.findall('.//a:blip',ns))
    d=Document(io.BytesIO(data))
    return {'xml_blocks':xml_blocks,'xml_text':xml_text,'media':media,'drawing_refs':drawings,'library_paragraphs':[p.text for p in d.paragraphs],'library_tables':[[[c.text for c in row.cells] for row in t.rows] for t in d.tables],'library_inline_shapes':len(d.inline_shapes)}

def main():
    md=Path(__file__).with_name('fixture.md').read_text(encoding='utf-8')
    a=MarkdownIt('commonmark',{'html':True}).enable('table').parse(md)
    def flatten(ts):
        for t in ts:
            yield {'type':t.type,'content':t.content,'attrs':t.attrs,'map':t.map}
            yield from flatten(t.children or [])
    tokens=list(flatten(a)); ast=mistune.create_markdown(renderer='ast',plugins=['table'])(md)
    def walk(nodes):
        for n in nodes:
            yield n
            yield from walk(n.get('children',[]))
    nodes=list(walk(ast)); data=make_docx(); d=docx_probe(data)
    result={'python':platform.python_version(),'versions':{m:version(m) for m in ['markdown-it-py','mistune','python-docx','Pillow']},'markdown_sha256':hashlib.sha256(md.encode()).hexdigest(),'markdown_it_types':sorted(set(t['type'] for t in tokens)),'mistune_types':sorted(set(n['type'] for n in nodes)),'markdown_it_links_images':[t for t in tokens if t['type'] in ('link_open','image')],'mistune_links_images':[n for n in nodes if n['type'] in ('link','image')],'docx':d}
    assert 'table_open' in result['markdown_it_types'] and 'table' in result['mistune_types']
    assert d['drawing_refs']==d['library_inline_shapes']==1 and d['library_tables']==[[['Feature','Value'],['Alpha','One']]]
    assert 'Alpha' in d['xml_text'] and not any('Alpha' in p for p in d['library_paragraphs'])
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
