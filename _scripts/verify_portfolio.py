from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
root = Path('_site')
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.links=[]; self.ids=set(); self.feed(text)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        for k in ['href','src']:
            if k in a:self.links.append(a[k])
errors=[]
for name in ['index.html','about/index.html','projects/index.html','cv/index.html','music/index.html']:
    path=root/name
    assert path.is_file(),f'Missing {path}'
    text=path.read_text();page=Page(text)
    assert '{{' not in text, f'Unrendered Liquid in {name}'
    for link in page.links:
        u=urlsplit(link)
        if u.scheme or u.netloc:continue
        dest=root/unquote(u.path.lstrip('/')) if u.path.startswith('/') else path.parent/unquote(u.path)
        if not u.path:dest=path
        if dest.is_dir():dest=dest/'index.html'
        if not dest.exists():errors.append(f'{name}: missing {link}')
        elif u.fragment and dest.suffix=='.html' and unquote(u.fragment) not in Page(dest.read_text()).ids:errors.append(f'{name}: missing anchor {link}')
    if name in ['index.html','projects/index.html','cv/index.html']:
        assert 'Blue Cheese' in text and 'Uncertainty' in text,name
    if name in ['about/index.html','cv/index.html']:
        assert 'May 2027' in text and 'Artificial Intelligence' in text,name
assert not errors,'\n'.join(errors)
for f in ['_data/cv.yml','assets/json/resume.json']:
    text=Path(f).read_text()
    assert not any(s in text for s in ['Nobel','Princeton','Theoretical Physics','Expected 2026']),f
assert (root/'assets/pdf/albert-yoshimoto-resume.pdf').read_bytes()==Path('assets/pdf/albert-yoshimoto-resume.pdf').read_bytes()
print('Verified homepage, about, projects, CV, music, local links, anchors and resume bytes.')
