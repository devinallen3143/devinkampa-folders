#!/usr/bin/env python3
"""Add (or refresh) the open-house sign-in card on a folder. Idempotent: replaces the block between
<!--SIGNIN-START--> and <!--SIGNIN-END-->.
Usage: python3 tools/flyers/add_signin.py <slug> [--agent "Taffney Wilson"] [--endpoint https://.../api/signin]
Takes a screenshot of the folder's open state as the blurred backdrop, then injects the card (CSS + HTML + JS).
Register the folder's agent first: tools/flyers/register_signin.py (sign-ins are emailed by folder slug)."""
import argparse, base64, io, os, re, sys, threading, http.server, socketserver, functools
from playwright.sync_api import sync_playwright
from PIL import Image, ImageFilter

ap = argparse.ArgumentParser(); ap.add_argument('slug'); ap.add_argument('--agent', default='')
ap.add_argument('--endpoint', default='https://steady-sundae-af3aa3.netlify.app/api/signin'); a = ap.parse_args()
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')); path = os.path.join(ROOT, a.slug, 'index.html')
html = open(path, encoding='utf-8').read()
html = re.sub(r'<!--SIGNIN-START-->.*?<!--SIGNIN-END-->', '', html, flags=re.S)  # screenshot the clean folder
open(path, 'w', encoding='utf-8').write(html)

class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *x): pass
socketserver.TCPServer.allow_reuse_address = True
srv = socketserver.TCPServer(('127.0.0.1', 0), functools.partial(Q, directory=ROOT)); PORT = srv.server_address[1]  # free port
threading.Thread(target=srv.serve_forever, daemon=True).start()

def backdrop(vp, mobile, scale):
    with sync_playwright() as p:
        b = p.chromium.launch(); ctx = b.new_context(viewport=vp, device_scale_factor=scale, is_mobile=mobile, has_touch=mobile); pg = ctx.new_page()
        pg.goto(f'http://127.0.0.1:{PORT}/{a.slug}/index.html'); pg.wait_for_timeout(1800)
        (pg.touchscreen.tap if mobile else pg.mouse.click)(vp['width'] // 2, vp['height'] // 2); pg.wait_for_timeout(800)
        pg.evaluate("document.getElementById('skipB').click()"); pg.wait_for_timeout(4200)
        png = pg.screenshot(); b.close()
    im = Image.open(io.BytesIO(png)).convert('RGB').filter(ImageFilter.GaussianBlur(1.2 * scale)); buf = io.BytesIO(); im.save(buf, 'JPEG', quality=72)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()
bd_desk = backdrop({'width': 1440, 'height': 900}, False, 1); bd_phone = backdrop({'width': 390, 'height': 844}, True, 2)
srv.shutdown()

consent_agent = a.agent or 'the listing agent'
CSS = '''<style id="so-css">
#so{position:fixed;inset:0;z-index:99990;display:flex;align-items:center;justify-content:center;padding:16px;background:#fff center top/cover no-repeat;background-image:url(__BD_DESK__);font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text","Helvetica Neue",Arial,sans-serif;color:#14181D;transition:opacity .45s ease}
#so::before{content:"";position:absolute;inset:0;background:rgba(255,255,255,.12)}
#so.soout{opacity:0;pointer-events:none}
#so,#so *{box-sizing:border-box}
#so .sop{position:relative;width:100%;max-width:372px;text-align:center;padding:26px 26px 20px;border-radius:20px;background:#eef1f4;box-shadow:0 24px 60px rgba(20,24,29,.22),0 2px 6px rgba(20,24,29,.08);border:1px solid rgba(20,24,29,.06)}
#so .soe{font-size:10.5px;letter-spacing:.22em;text-transform:uppercase;color:#1f6bf0;font-weight:600;margin:0 0 6px}
#so h1{font-family:'CormorantCover',Georgia,serif;font-weight:500;font-size:34px;line-height:1.05;margin:2px 0 12px;letter-spacing:-.005em;color:#14181D}
#so form{text-align:left;margin:0}
#so .sof{margin:0 0 7px}
#so label{display:block;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#5a6370;font-weight:600;margin:0 0 4px}
#so input[type=text],#so input[type=tel],#so input[type=email]{width:100%;height:42px;border:1px solid #d5dbe3;border-radius:10px;padding:0 14px;font:inherit;font-size:16px;color:#14181D;background:#fff;outline:none;margin:0;-webkit-appearance:none;appearance:none}
#so input::placeholder{color:#a3abb6}
#so input:focus{border-color:#1f6bf0;box-shadow:0 0 0 3px rgba(31,107,240,.18)}
#so .sof.sobad input{border-color:#B3261E;box-shadow:0 0 0 3px rgba(179,38,30,.10)}
#so .som{display:none;font-size:12.5px;color:#B3261E;margin:5px 2px 0}
#so .sof.sobad .som{display:block}
#so .sohp{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}
#so .sob{width:100%;height:46px;margin-top:6px;border:0;border-radius:999px;background:linear-gradient(180deg,#3d8bff,#1f6bf0);color:#fff;font:inherit;font-size:15px;font-weight:600;cursor:pointer;box-shadow:0 8px 20px rgba(31,107,240,.38)}
#so .sob[disabled]{opacity:.7;cursor:default}
#so .sos{display:block;margin:12px auto 0;background:none;border:0;color:#5a6370;font:inherit;font-size:13px;text-decoration:underline;text-underline-offset:3px;cursor:pointer;padding:2px 6px}
#so .sofn{font-size:11px;line-height:1.5;color:#7b8491;margin:12px 2px 0;text-align:center}
@media (max-aspect-ratio:1/1){#so{background-image:url(__BD_PHONE__)}}
@media(max-width:480px){#so{align-items:flex-end;padding:12px 18px 54px}#so .sop{max-width:330px;padding:16px 18px 12px;border-radius:18px}#so .soe{font-size:9.5px;margin:0 0 3px}#so h1{font-size:27px;margin:0 0 10px}#so label{font-size:9.5px;margin-bottom:3px}#so .sof{margin:0 0 6px}#so input[type=text],#so input[type=tel],#so input[type=email]{height:38px;border-radius:9px}#so .sob{height:42px;font-size:14px;margin-top:4px}#so .sos{margin-top:9px;font-size:12px}#so .sofn{font-size:9.5px;margin:9px 0 0}}
#legal{z-index:99995!important}
</style>'''.replace('__BD_DESK__', bd_desk).replace('__BD_PHONE__', bd_phone)
HTML = '''<div id="so" role="dialog" aria-modal="true" aria-labelledby="so-h"><div class="sop">
<p class="soe">Open House</p><h1 id="so-h">Please sign in.</h1>
<form id="so-f" novalidate autocomplete="on">
<div class="sof" data-k="name"><label for="so-n">Name</label><input id="so-n" name="name" type="text" autocomplete="name" placeholder="First and last name"><div class="som"></div></div>
<div class="sof" data-k="phone"><label for="so-p">Phone</label><input id="so-p" name="tel" type="tel" inputmode="tel" autocomplete="tel" placeholder="(555) 123-4567"><div class="som"></div></div>
<div class="sof" data-k="email"><label for="so-e">Email</label><input id="so-e" name="email" type="email" inputmode="email" autocomplete="email" placeholder="name@email.com"><div class="som"></div></div>
<div class="sohp" aria-hidden="true"><input id="so-hp" name="website" type="text" tabindex="-1" autocomplete="off"></div>
<button class="sob" type="submit">Sign in and view the folder</button>
<button class="sos" type="button" id="so-skip">Skip for now</button>
<p class="sofn">By signing in, you agree to be contacted by Devin Kampa and __AGENT__ about this property. Message and data rates may apply.</p>
</form></div></div>'''.replace('__AGENT__', consent_agent)
JS = '''<script id="so-js">(function(){
var EP="__EP__",SLUG="__SLUG__",K="so:"+SLUG,box=document.getElementById("so");if(!box)return;
function get(){try{return localStorage.getItem(K)}catch(e){return null}}function set(){try{localStorage.setItem(K,String(Date.now()))}catch(e){}}
var KS="so-skip:"+SLUG,root=document.documentElement;
function sk(){try{return sessionStorage.getItem(KS)}catch(e){return null}}
try{if(/[?&]signin=1\\b/.test(location.search)){localStorage.removeItem(K);sessionStorage.removeItem(KS)}}catch(e){}
function drop(){if(box.parentNode)box.parentNode.removeChild(box);var c=document.getElementById("so-css");if(c)c.parentNode.removeChild(c)}
function close(){box.classList.add("soout");setTimeout(drop,520)}
// Save (PDF download) is only for people who signed in. Anyone who hasn't (skipped, or not yet asked) has no Save button.
if(!get()){var ns=document.createElement("style");ns.id="so-ns";ns.textContent=".so-nosave #dlB{display:none!important}";document.head.appendChild(ns);root.classList.add("so-nosave")}
function signedIn(){set();root.classList.remove("so-nosave");close()}
if(get()||sk()){drop();return}
var form=document.getElementById("so-f"),$=function(id){return document.getElementById(id)};
function row(k){return form.querySelector('[data-k="'+k+'"]')}
function bad(k,m){var r=row(k);r.classList.add("sobad");r.querySelector(".som").textContent=m;return false}
function ok(k){row(k).classList.remove("sobad");return true}
var FAKE=/^(example|test|pewpew|asdf|fake|invalid|mailinator|tempmail|guerrillamail|10minutemail|yopmail|trashmail|throwaway|sharklasers|getnada|maildrop)\\./i;
var TYPO={"gmial.com":"gmail.com","gmal.com":"gmail.com","gamil.com":"gmail.com","gmail.co":"gmail.com","yaho.com":"yahoo.com","yahooo.com":"yahoo.com","hotmial.com":"hotmail.com","outlok.com":"outlook.com","icloud.co":"icloud.com"};
function vName(){var v=$("so-n").value.trim().replace(/\\s+/g," ");if(!/^[A-Za-z\\u00C0-\\u024F'\\u2019.-]{2,}( [A-Za-z\\u00C0-\\u024F'\\u2019. -]{2,})+$/.test(v)||/^(test|asdf|qwer|none|na|n\\/a|john doe|jane doe)\\b/i.test(v))return bad("name","Please enter your first and last name.");return ok("name")}
function digits(){return $("so-p").value.replace(/\\D/g,"").replace(/^1(?=\\d{10}$)/,"")}
function vPhone(){var d=digits(),a=d.slice(0,3),x=d.slice(3,6),l=d.slice(6);
var f=d.length!==10||/^[01]/.test(a)||/^[01]/.test(x)||/^(\\d)\\1{9}$/.test(d)||"1234567890,0123456789,9876543210".indexOf(d)>-1||a==="555"||(x==="555"&&/^01\\d\\d$/.test(l))||/^(\\d)\\1\\1$/.test(a)||new Set(d.split("")).size<=2;
if(f)return bad("phone","That number doesn\\u2019t look right. Please enter a real mobile number.");return ok("phone")}
function vEmail(){var v=$("so-e").value.trim().toLowerCase(),m=v.match(/^[a-z0-9._%+-]+@([a-z0-9-]+(\\.[a-z0-9-]+)*\\.[a-z]{2,})$/);
if(!m||v.indexOf("..")>-1||v.indexOf("@.")>-1||v.charAt(0)==="."||FAKE.test(m[1]))return bad("email","Please enter a valid email address.");
if(TYPO[m[1]])return bad("email","Did you mean "+v.split("@")[0]+"@"+TYPO[m[1]]+"?");return ok("email")}
// no validate-on-blur: an error appearing/disappearing mid-tap shifts the layout and makes the tap miss the button. Errors show on submit and clear as the person types.
["name","phone","email"].forEach(function(k){row(k).querySelector("input").addEventListener("input",function(){row(k).classList.remove("sobad")})});
$("so-p").addEventListener("input",function(e){var d=e.target.value.replace(/\\D/g,"").replace(/^1(?=\\d{10})/,"").slice(0,10);e.target.value=d.length>6?"("+d.slice(0,3)+") "+d.slice(3,6)+"-"+d.slice(6):d.length>3?"("+d.slice(0,3)+") "+d.slice(3):d});
$("so-skip").addEventListener("click",function(){try{sessionStorage.setItem(KS,"1")}catch(e){}close()});
form.addEventListener("submit",function(ev){ev.preventDefault();var r=[vName(),vPhone(),vEmail()];if(r.indexOf(false)>-1)return;
var btn=form.querySelector(".sob");btn.disabled=true;btn.textContent="Signing in\\u2026";
var body=JSON.stringify({slug:SLUG,name:$("so-n").value.trim(),phone:$("so-p").value,email:$("so-e").value.trim(),consent:true,hp:$("so-hp").value});
fetch(EP,{method:"POST",headers:{"Content-Type":"application/json"},body:body}).then(function(res){
 if(res.status===422){return res.json().then(function(j){var e=j.errors||{};btn.disabled=false;btn.textContent="Sign in and view the folder";
  if(e.name)bad("name",e.name);if(e.phone)bad("phone",e.phone);if(e.email)bad("email",e.email)})}
 btn.textContent="Thank you";setTimeout(signedIn,500)
}).catch(function(){btn.textContent="Thank you";setTimeout(signedIn,500)})});
})();</script>'''.replace('__EP__', a.endpoint).replace('__SLUG__', a.slug)
block = '<!--SIGNIN-START-->' + CSS + HTML + JS + '<!--SIGNIN-END-->'
i = html.rindex('</body>'); html = html[:i] + block + html[i:]
open(path, 'w', encoding='utf-8').write(html); print('sign-in added to', a.slug, len(block) // 1024, 'KB')
