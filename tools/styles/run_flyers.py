import subprocess,os,json,sys
from palettes import PAL
for k,p in PAL.items():
    env=dict(os.environ,PAL=json.dumps(p))
    print(subprocess.run(['python3','render_theme.py','t2_metropolitan'],env=env,capture_output=True,text=True).stdout.strip())
