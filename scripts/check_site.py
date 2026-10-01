"""Check public HTML structure and local asset links without extra packages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parents[1]
VOID = set('area base br col embed hr img input link meta param source track wbr'.split())
errors = []

class CheckHTML(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.stack, self.ids = path, [], set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag not in VOID:
            self.stack.append(tag)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                errors.append(f'{self.path.name}: duplicate id {attrs["id"]}')
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            value = attrs.get(key, '')
            url = urlsplit(value)
            if value and not url.scheme and not url.netloc and url.path:
                target = ROOT / unquote(url.path.lstrip('/')) if url.path.startswith('/') else self.path.parent / unquote(url.path)
                if not target.exists():
                    errors.append(f'{self.path.name}: missing {value}')
        if tag == 'iframe' and not attrs.get('title'):
            errors.append(f'{self.path.name}: iframe has no title')

    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1] != tag:
            errors.append(f'{self.path.name}: unexpected </{tag}>')
        else:
            self.stack.pop()

for path in sorted(ROOT.glob('*.html')):
    parser = CheckHTML(path)
    parser.feed(path.read_text())
    if parser.stack:
        errors.append(f'{path.name}: unclosed tags {parser.stack}')
for value in re.findall(r'url\(([^)]+)\)', (ROOT / 'css/main.css').read_text()):
    if not (ROOT / 'css' / value.strip('\"\'')).exists():
        errors.append(f'CSS: missing {value}')
if errors:
    raise SystemExit('\n'.join(errors))
print('PASS: public HTML structure, unique IDs, iframe titles, local links and CSS images.')
