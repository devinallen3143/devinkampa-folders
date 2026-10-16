#!/usr/bin/env python3
"""Straighten + enhance an uploaded agent business-card photo (HEIC/JPG/PNG) into a clean 3.5x2 card image.
Usage: python3 tools/flyers/prep_card.py card.heic out.jpg [--corners x1,y1,x2,y2,x3,y3,x4,y4]   (TL,TR,BR,BL in source px)
Without --corners it tries to detect the card (bright quad); check the result by eye, and pass corners if the crop is off.
Output is the EXACT uploaded card (never recreated), 1400x800."""
import sys, argparse, cv2, numpy as np
from PIL import Image, ImageOps
try:
    from pillow_heif import register_heif_opener; register_heif_opener()
except ImportError: pass
ap = argparse.ArgumentParser(); ap.add_argument('src'); ap.add_argument('out'); ap.add_argument('--corners'); a = ap.parse_args()
im = cv2.cvtColor(np.array(ImageOps.exif_transpose(Image.open(a.src)).convert('RGB')), cv2.COLOR_RGB2BGR)
h, w = im.shape[:2]
if a.corners: q = np.float32(a.corners.split(',')).reshape(4, 2)
else:
    g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY); _, t = cv2.threshold(g, 110, 255, cv2.THRESH_BINARY)
    t = cv2.morphologyEx(t, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    c = max(cv2.findContours(t, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0], key=cv2.contourArea)
    box = cv2.boxPoints(cv2.minAreaRect(c)); s = box.sum(1); d = np.diff(box, axis=1).ravel()
    q = np.float32([box[s.argmin()], box[d.argmin()], box[s.argmax()], box[d.argmax()]])
    cen = q.mean(0); q = cen + (q - cen) * 0.985
W, H = 2100, 1200
o = cv2.warpPerspective(im, cv2.getPerspectiveTransform(q, np.float32([[0, 0], [W, 0], [W, H], [0, H]])), (W, H), flags=cv2.INTER_CUBIC)
o = cv2.fastNlMeansDenoisingColored(o, None, 3, 3, 7, 21)
f = o.astype(np.float32); ref = np.percentile(f[int(H*.2):int(H*.85), int(W*.5):].reshape(-1, 3), 75, axis=0)
f = np.clip(f / ref * 248, 0, 255); f = 255 * np.power(f / 255, 1.12)
o = np.clip(f, 0, 255).astype(np.uint8); o = cv2.addWeighted(o, 1.55, cv2.GaussianBlur(o, (0, 0), 1.4), -0.55, 0)
o = cv2.resize(o, (1400, 800), interpolation=cv2.INTER_AREA)
cv2.imwrite(a.out, o, [cv2.IMWRITE_JPEG_QUALITY, 90]); print('wrote', a.out)
