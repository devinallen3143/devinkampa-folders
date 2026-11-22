import sys,os
from common import render
import light,lay_azure,lay_terra,lay_evergreen
B={'metropolitan':lambda:light.build('metropolitan'),'azure':lay_azure.build,'terra':lay_terra.build,'evergreen':lay_evergreen.build}
for n in sys.argv[1:]:
    os.makedirs(f'out/{n}',exist_ok=True)
    d={k:light.postproc(n,v,k) for k,v in B[n]().items()}
    render([(f'/home/claude/work/styles/out/{n}/{k}.jpg',h) for k,h in d.items()]); print('ok',n)
