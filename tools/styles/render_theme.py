import sys, importlib, os
sys.path.insert(0,'/home/claude/work/styles')
from common import render
t=sys.argv[1]; m=importlib.import_module(t)
os.makedirs(f'out/{m.NAME}',exist_ok=True)
render([(f'/home/claude/work/styles/out/{m.NAME}/{k}.jpg',h) for k,h in m.all().items()])
print('rendered',m.NAME)
