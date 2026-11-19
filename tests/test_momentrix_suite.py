"""Comprehensive Test Suite for Momentrix

Verifies:
1. Cyber Defense & Threat Interception (Path traversal, XSS/SQLi in queries, null bytes)
2. Security Headers & Cache-Busting Headers
3. Single-User Root Access & Authentication Neutrality (No login wall)
4. Core API Endpoints (/healthz, /api/status, /api/overview, /api/sync, /api/creators)
5. Brand Assets & SVG Logos
6. UI DOM Integrity & Interactive Elements (Buttons, Inputs, Modals, Steppers, Caption Styles)
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "http://127.0.0.1:8765"
ORIGIN = {"Origin": BASE, "Content-Type": "application/json"}

passed = 0
failed = 0
failures = []


def assert_test(name: str, condition: bool, details: str = ""):
    global passed, failed
    if condition:
        passed += 1
        print(f"  [PASS] {name}")
    else:
        failed += 1
        msg = f"  [FAIL] {name}" + (f" ({details})" if details else "")
        print(msg)
        failures.append(name)


def req(path: str, method: str = "GET", data: dict = None, headers: dict = None, follow_redirects: bool = False):
    import http.client
    conn = http.client.HTTPConnection("127.0.0.1", 8765, timeout=5)
    h = headers.copy() if headers else {}
    body = json.dumps(data) if data is not None else None
    if body and "Content-Type" not in h:
        h["Content-Type"] = "application/json"
    try:
        conn.request(method, path, body=body, headers=h)
        resp = conn.getresponse()
        resp_headers = {k.lower(): v for k, v in resp.getheaders()}
        resp_body = resp.read().decode("utf-8", errors="replace")
        conn.close()
        return resp.status, resp_headers, resp_body
    except Exception as e:
        return 0, {}, str(e)


print("\n========================================================")
print("  MOMENTRIX COMPREHENSIVE TEST SUITE")
print("========================================================\n")

# -------------------------------------------------------------------------
# Test Group 1: Cyber Defense & Security Gatekeeper
# -------------------------------------------------------------------------
print("--- Group 1: Cyber Defense & Security Gatekeeper ---")

# 1.1 Path Traversal Blocking
status, h, body = req("/app/..")
assert_test("Blocks path traversal '..' in URL", status == 400, f"got {status}")

status, h, body = req("/app/%2e%2e/secret")
assert_test("Blocks URL-encoded path traversal '%2e%2e'", status == 400, f"got {status}")

status, h, body = req("/api/status?path=../../etc/passwd")
assert_test("Blocks query traversal '../../'", status == 400, f"got {status}")

# 1.2 Injection Blocking (XSS & SQLi)
status, h, body = req("/api/status?q=<script>alert(1)</script>")
assert_test("Blocks XSS '<script>' injection in queries", status == 400, f"got {status}")

status, h, body = req("/api/status?token=javascript:void(0)")
assert_test("Blocks 'javascript:' pseudo-protocol payload", status == 400, f"got {status}")

status, h, body = req("/api/status?search=1%20UNION%20SELECT%20*%20FROM%20users")
assert_test("Blocks SQLi 'UNION SELECT' token", status == 400, f"got {status}")

# 1.3 Security Headers
status, h, body = req("/app")
assert_test("Header X-Content-Type-Options: nosniff", h.get("x-content-type-options") == "nosniff")
assert_test("Header X-Frame-Options: DENY", h.get("x-frame-options") == "DENY")
assert_test("Header X-XSS-Protection: 1; mode=block", h.get("x-xss-protection") == "1; mode=block")
assert_test("Header X-Permitted-Cross-Domain-Policies: none", h.get("x-permitted-cross-domain-policies") == "none")
assert_test("Header Referrer-Policy: strict-origin-when-cross-origin", h.get("referrer-policy") == "strict-origin-when-cross-origin")
assert_test("Header Content-Security-Policy present", "content-security-policy" in h)
assert_test("Header Permissions-Policy present", "permissions-policy" in h)

# 1.4 Cache-Busting Headers on Dynamic Pages
assert_test("Page /app has no-cache, no-store headers", "no-store" in h.get("cache-control", ""))

# -------------------------------------------------------------------------
# Test Group 2: Single-User Direct Access & Auth Neutrality
# -------------------------------------------------------------------------
print("\n--- Group 2: Single-User Direct Access & Auth Neutrality ---")

status, h, body = req("/app")
assert_test("Direct access to /app with HTTP 200 (No login wall)", status == 200)

status, h, body = req("/login")
assert_test("/login redirects to /app", status in (302, 303) and h.get("location") == "/app")

status, h, body = req("/signup")
assert_test("/signup redirects to /app", status in (302, 303) and h.get("location") == "/app")

status, h, body = req("/reset")
assert_test("/reset redirects to /app", status in (302, 303) and h.get("location") == "/app")

status, h, body = req("/api/status")
st = json.loads(body) if status == 200 else {}
assert_test("API status confirms accounts=False", st.get("accounts") is False)
assert_test("Current user is administrator", st.get("user", {}).get("is_admin") is True)
assert_test("Current user name is 'You'", st.get("user", {}).get("name") == "You")

# -------------------------------------------------------------------------
# Test Group 3: Core API Endpoints & CRUD
# -------------------------------------------------------------------------
print("\n--- Group 3: Core API Endpoints & CRUD ---")

status, h, body = req("/healthz")
assert_test("/healthz returns HTTP 200", status == 200)

status, h, body = req("/api/sync")
sync_data = json.loads(body) if status == 200 else {}
assert_test("/api/sync returns valid status", status == 200 and "v" in sync_data)

status, h, body = req("/api/overview")
ov_data = json.loads(body) if status == 200 else {}
assert_test("/api/overview returns stats", status == 200 and "recording" in ov_data)

# Create a test creator workspace
status, h, body = req("/api/creators", method="POST", data={"name": "TestCreator", "channel": "https://youtube.com/@test"}, headers=ORIGIN)
assert_test("Create creator workspace returns HTTP 200", status == 200)
c_data = json.loads(body) if status == 200 else {}
assert_test("Created creator has valid id and name", c_data.get("name") == "TestCreator" and "id" in c_data)

# Clean up created creator if id present
if c_data.get("id"):
    req(f"/api/creators/{c_data['id']}", method="DELETE", headers=ORIGIN)

# -------------------------------------------------------------------------
# Test Group 4: Brand Assets & Static Content
# -------------------------------------------------------------------------
print("\n--- Group 4: Brand Assets & Static Content ---")

status, h, body = req("/brand/logo-light.svg")
assert_test("/brand/logo-light.svg returns HTTP 200", status == 200 and "image/svg+xml" in h.get("content-type", ""))

status, h, body = req("/brand/favicon.svg")
assert_test("/brand/favicon.svg returns HTTP 200", status == 200 and "image/svg+xml" in h.get("content-type", ""))

status, h, body = req("/robots.txt")
assert_test("/robots.txt returns HTTP 200 with text/plain", status == 200 and "text/plain" in h.get("content-type", ""))

# -------------------------------------------------------------------------
# Test Group 5: UI DOM Integrity & Interactive Elements
# -------------------------------------------------------------------------
print("\n--- Group 5: UI DOM Integrity & Interactive Elements ---")

html_path = Path("web/index.html")
assert_test("web/index.html exists", html_path.exists())
html = html_path.read_text(encoding="utf-8")

# Check Cyber Guard elements
assert_test("Cyber Guard dialog <dialog id='guarddlg'> exists in HTML", 'id="guarddlg"' in html)
assert_test("Cyber Guard dialog class 'cyber-guard-dlg' exists", 'class="cyber-guard-dlg"' in html)
assert_test("Cyber Shield Active pill badge exists in Topbar", "Shield Active" in html and 'data-act="shieldinfo"' in html)
assert_test("JavaScript verifyRoute function defined", "function verifyRoute(" in html)
assert_test("JavaScript showCyberGuardNotice function defined", "function showCyberGuardNotice(" in html)
assert_test("Cyber Guard reset button action defined", 'data-act="guardreset"' in html)

# Check Composer controls and buttons
assert_test("URL input field #url exists", 'id="url"' in html)
assert_test("Upload video button with data-act='pickfile' exists", 'data-act="pickfile"' in html)
assert_test("Studio Options toggle with data-act='toggleopts' exists", 'data-act="toggleopts"' in html)
assert_test("Generate Clips button #goBtn exists", 'id="goBtn"' in html)

# Check Stepper numeric inputs
assert_test("Stepper 'o_max' (Max Clips) exists", 'id="o_max"' in html or 'o_max' in html)
assert_test("Stepper 'o_min' (Min Length) exists", 'id="o_min"' in html or 'o_min' in html)
assert_test("Stepper 'o_maxlen' (Max Length) exists", 'id="o_maxlen"' in html or 'o_maxlen' in html)

# Check Subtitle Styles
for style in ("bounce", "hype", "clean", "hormozi", "neon"):
    assert_test(f"Subtitle style '{style}' present in CAP_LOOK", f"{style}:" in html)

# Check Layout Modes
for lay in ("blur", "zoom", "crop", "gameplay"):
    assert_test(f"Layout mode '{lay}' present in LAYOUT_SHORT", f"{lay}:" in html)

# Check Video Quality Segments
assert_test("Video Quality 720p HD option exists", '720p' in html)
assert_test("Video Quality 1080p Ultra option exists", '1080p' in html)

# Check Aspect Framing & Time Range
assert_test("Time range inputs #o_from and #o_to exist", 'id="o_from"' in html and 'id="o_to"' in html)

# Check Root index.html synchronicity
root_html = Path("index.html").read_text(encoding="utf-8")
assert_test("web/index.html and root index.html are identical in size", len(html) == len(root_html))

print("\n========================================================")
print(f"  TEST RESULTS: {passed} PASSED, {failed} FAILED")
print("========================================================\n")

if failures:
    print("Failed Tests:")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
else:
    print("All test cases passed successfully with 100% compliance!")
    sys.exit(0)
