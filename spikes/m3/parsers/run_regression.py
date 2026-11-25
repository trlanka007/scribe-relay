"""Run isolated M3 parser experiments and record reproducibility evidence."""
import hashlib
import json
import platform
import subprocess
import sys
from importlib.metadata import version, PackageNotFoundError
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXPECTED = {
    "safety_probe.py": "ee9d3a953b294fbf9c2cba3de54548fe511ceedd",
    "opc_probe.py": "cf5c48a6ec1623e2c7a89bbfab256db81c599b05",
    "integrated_probe.py": "cba2614ab39575a3a4a6ffa19823988fb1106bf1",
    "package_probe.py": "ea634c302ae6a6a31237d5fe7462aaa27e30949e",
    "generated_probe.py": "a058788dd08819a87c92fc0da0c8137e6c58c2f2",
    "markdown_probe.py": "d3feb144e03e70b9d99ec0800c7d5e25ec4ec38f",
    "disposition_probe.py": "7f5f605728ba3e816b114f5c1b650a1c18162888",
    "compare.py": "1553fbd66df91a3f4318a674345ab9953b5c231e",
    "fixture.md": "783bc9d63f45425fa41aa27d8e4237f7f63131da",
    "requirements.txt": "9a763a05332a1553a86db983e5832a1ef37e7031"
}
SCRIPTS = ["safety_probe.py","opc_probe.py","integrated_probe.py","package_probe.py","generated_probe.py","markdown_probe.py","disposition_probe.py","compare.py"]

def blob_sha(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()

def installed(name):
    try:
        return version(name)
    except PackageNotFoundError:
        return None

def main():
    pins = dict(line.split("==",1) for line in (ROOT/"requirements.txt").read_text().splitlines() if line.strip())
    versions = {name:installed(name) for name in pins}
    actual = {name:blob_sha(ROOT/name) for name in EXPECTED}
    result = {"python":platform.python_version(), "platform":platform.platform(),
              "pins":pins, "installed":versions, "pins_match":versions==pins,
              "expected_blobs":EXPECTED, "actual_blobs":actual,
              "blobs_match":actual==EXPECTED, "runs":[]}
    if result["blobs_match"]:
        for script in SCRIPTS:
            try:
                p = subprocess.run([sys.executable,"-B",str(ROOT/script)],cwd=ROOT,
                                   capture_output=True,text=True,encoding="utf-8",errors="replace",
                                   timeout=60)
                result["runs"].append({"script":script,"returncode":p.returncode,
                                       "stdout":p.stdout,"stderr":p.stderr})
            except subprocess.TimeoutExpired:
                result["runs"].append({"script":script,"returncode":None,"error":"timeout"})
    print(json.dumps(result,ensure_ascii=True,indent=2))
    return 0 if (result["pins_match"] and result["blobs_match"] and
                 len(result["runs"])==len(SCRIPTS) and
                 all(run["returncode"]==0 for run in result["runs"])) else 1

if __name__=="__main__":
    raise SystemExit(main())
