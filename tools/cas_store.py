# tools/cas_store.py  — content-addressed artifacts: machines that check machines
import hashlib, shutil, json
from pathlib import Path
def put(path, root=Path(".cas")):
    b = Path(path).read_bytes(); sha = hashlib.sha256(b).hexdigest()
    dest = root / sha[:2] / sha
    dest.parent.mkdir(parents=True, exist_ok=True); dest.write_bytes(b)
    return sha
