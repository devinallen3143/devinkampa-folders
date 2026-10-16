#!/usr/bin/env python3
"""Register a folder's agent with the sign-in endpoint so sign-ins email that agent + Devin.
Usage: python3 tools/flyers/register_signin.py <slug> tools/flyers/listings/<slug>.json [--repo /home/claude/devinkampa-signin]
Writes <repo>/agents.json (private repo devinallen3143/devinkampa-signin), then commit + push that repo.
No agent card (blank example agent) = Devin only is emailed."""
import json, sys, os, argparse
ap = argparse.ArgumentParser(); ap.add_argument('slug'); ap.add_argument('config'); ap.add_argument('--repo', default='/home/claude/devinkampa-signin'); a = ap.parse_args()
cfg = json.load(open(a.config)); ag = cfg.get('agent') or {}
p = os.path.join(a.repo, 'agents.json'); d = json.load(open(p)) if os.path.exists(p) else {}
d[a.slug] = {'address': cfg['address'], 'agent': ({'name': ag.get('name', ''), 'email': ag.get('email', ''), 'phone': ag.get('phone', ''), 'brokerage': ag.get('brokerage', '')} if ag.get('email') else {})}
json.dump(d, open(p, 'w'), indent=2, ensure_ascii=False); print('registered', a.slug, '->', d[a.slug]['agent'].get('email') or '(Devin only)')
