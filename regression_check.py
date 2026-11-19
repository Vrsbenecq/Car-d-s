"""Non-destructive static regression check. Run: python regression_check.py"""
from pathlib import Path
import subprocess, tempfile, re, sys
root=Path(__file__).resolve().parent
html=(root/'index.html').read_text()
sw=(root/'sw.js').read_text()
checks={
 '13.5 cache revision': "car-supercard-135" in sw,
 'Collection overview retained': 'overview132()' in html,
 'Collection catalog retained': 'draw132()' in html,
 'Collection filters retained': 'collection-brand' in html and 'collection-search' in html,
 'Draft Arena retained': 'draft-focus1311' in html,
 'Save logic retained': 'function save(' in html,
 'No broken 13.4 toolbar transplant': 'collection134-tools' not in html,
}
for k,v in checks.items():print(('PASS' if v else 'FAIL'),k)
# Extract each inline script for syntax validation without executing gameplay.
scripts=re.findall(r'<script(?:\s[^>]*)?>(.*?)</script\s*>',html,re.S|re.I)
for i,script in enumerate(scripts):
 if not script.strip():continue
 with tempfile.NamedTemporaryFile(suffix='.js',mode='w',delete=False) as f:
  f.write(script); name=f.name
 p=subprocess.run(['node','--check',name],capture_output=True,text=True)
 Path(name).unlink(missing_ok=True)
 checks[f'inline script {i} syntax']=p.returncode==0
 print(('PASS' if p.returncode==0 else 'FAIL'),f'inline script {i} syntax',p.stderr[:200] if p.returncode else '')
p=subprocess.run(['node','--check',str(root/'sw.js')],capture_output=True,text=True)
checks['service worker syntax']=p.returncode==0
print(('PASS' if p.returncode==0 else 'FAIL'),'service worker syntax')
sys.exit(0 if all(checks.values()) else 1)
