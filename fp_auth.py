"""Password gate for the Family Planner (added 2026-10-06 after the security audit).

Only requests that arrive through nginx (they carry X-Real-IP) are gated; scripts on the box
that call 127.0.0.1:8766 directly keep working. A correct password sets a one-year cookie.
"""
import hashlib, hmac, json, os, secrets, urllib.parse

AUTH_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".auth.json")
COOKIE = "fp_auth"


def _cfg():
    with open(AUTH_FILE) as f:
        return json.load(f)


def _hash(pw, salt):
    return hashlib.scrypt(pw.encode(), salt=bytes.fromhex(salt), n=2**14, r=8, p=1).hex()


def set_password(pw):
    salt = secrets.token_hex(16)
    data = {"salt": salt, "hash": _hash(pw, salt), "token": secrets.token_urlsafe(32)}
    with open(AUTH_FILE, "w") as f:
        json.dump(data, f)
    os.chmod(AUTH_FILE, 0o600)


def _cookie_ok(handler):
    raw = handler.headers.get("Cookie", "")
    for part in raw.split(";"):
        k, _, v = part.strip().partition("=")
        if k == COOKIE:
            return hmac.compare_digest(v, _cfg()["token"])
    return False


LOGIN_HTML = """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Family Planner</title><style>
body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;
font-family:-apple-system,system-ui,sans-serif;background:#fdf6ec;color:#3a2e22}
form{background:#fff;padding:28px 24px;border-radius:18px;box-shadow:0 8px 30px rgba(0,0,0,.08);
width:min(320px,calc(100vw - 32px));box-sizing:border-box}
h1{font-size:22px;margin:0 0 16px}input{width:100%;box-sizing:border-box;font-size:18px;
padding:12px;border:1px solid #d8cbb8;border-radius:10px;margin-bottom:12px}
button{width:100%;font-size:18px;padding:12px;border:0;border-radius:10px;background:#e07a3f;color:#fff}
p{color:#b3261e;margin:0 0 12px}</style></head><body>
<form method="post" action="/login"><h1>Family Planner</h1>%ERR%
<input type="password" name="password" placeholder="Password" autofocus autocomplete="current-password">
<button type="submit">Open</button></form></body></html>"""


def gate(handler, method):
    """Return True if the request may continue; otherwise the response has been sent."""
    if not handler.headers.get("X-Real-IP"):
        return True
    path = urllib.parse.urlparse(handler.path).path
    if path == "/login":
        if method == "POST":
            n = int(handler.headers.get("Content-Length") or 0)
            form = urllib.parse.parse_qs(handler.rfile.read(n).decode())
            pw = (form.get("password") or [""])[0]
            c = _cfg()
            if hmac.compare_digest(_hash(pw, c["salt"]), c["hash"]):
                handler.send_response(303)
                handler.send_header("Set-Cookie", f"{COOKIE}={c['token']}; Max-Age=31536000; Path=/; Secure; HttpOnly; SameSite=Lax")
                handler.send_header("Location", "/")
                handler.send_header("Content-Length", "0")
                handler.end_headers()
                return False
            return _login_page(handler, 401, "<p>Wrong password, try again.</p>")
        return _login_page(handler, 200, "")
    if _cookie_ok(handler):
        return True
    if path.startswith("/api/"):
        body = b'{"error":"login required"}'
        handler.send_response(401)
        handler.send_header("Content-Type", "application/json")
        handler.send_header("Content-Length", str(len(body)))
        handler.end_headers()
        handler.wfile.write(body)
        return False
    handler.send_response(302)
    handler.send_header("Location", "/login")
    handler.send_header("Content-Length", "0")
    handler.end_headers()
    return False


def _login_page(handler, code, err):
    body = LOGIN_HTML.replace("%ERR%", err).encode()
    handler.send_response(code)
    handler.send_header("Content-Type", "text/html; charset=utf-8")
    handler.send_header("Cache-Control", "no-store")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)
    return False
