"""Check public artifact integrity without third-party dependencies."""
from pathlib import Path
import hashlib,json,datetime
root=Path(__file__).resolve().parents[1]
catalog=json.loads((root/'catalogo.json').read_text(encoding='utf-8'))['documentos']
assert len(catalog)==23
assert len({r['id'] for r in catalog})==23
assert len({r['arquivo'] for r in catalog})==23
for r in catalog:
 p=root/r['arquivo'];assert p.resolve().is_relative_to(root.resolve())
 assert p.read_bytes().startswith(b'%PDF-')
 assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'],r['arquivo']
 if r['conclusao']:datetime.date.fromisoformat(r['conclusao'])
assert {p.relative_to(root).as_posix() for p in (root/'documentos').rglob('*') if p.is_file()}=={r['arquivo'] for r in catalog}
print('23 PDFs: paths, metadata dates and SHA-256 verified.')
