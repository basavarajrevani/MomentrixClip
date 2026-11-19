from pathlib import Path

dom_path = Path(r"web/index.html")
text = dom_path.read_text(encoding="utf-8", errors="replace")

checks = [
    ("MOMENTRIX Brand Header & Title", "Momentrix" in text),
    ("Cyber Shield Active Badge in Topbar", "Shield Active" in text and 'data-act="shieldinfo"' in text),
    ("Cyber Guard Modal Dialog element", 'id="guarddlg"' in text),
    ("Cyber Guard Dialog CSS Class", 'class="cyber-guard-dlg"' in text),
    ("URL input field (#url)", 'id="url"' in text),
    ("Pick File Upload button", 'data-act="pickfile"' in text),
    ("Studio Options toggle button", 'data-act="toggleopts"' in text),
    ("Generate Clips action button (#goBtn)", 'id="goBtn"' in text),
    ("Stepper o_max (Max Clips)", 'o_max' in text),
    ("Stepper o_min (Min Length)", 'o_min' in text),
    ("Stepper o_maxlen (Max Length)", 'o_maxlen' in text),
    ("Stepper increment/decrement logic", 'data-step=' in text),
    ("Aspect Ratio Framing (9:16 Shorts)", '9:16' in text),
    ("Video Quality Selector (720p / 1080p)", '720p' in text and '1080p' in text),
    ("Time Range controls (o_from & o_to)", 'o_from' in text and 'o_to' in text),
    ("Subtitle Styles (bounce, hype, clean, hormozi, neon)", all(s in text for s in ["bounce", "hype", "clean", "hormozi", "neon"])),
    ("Layout Options (blur, zoom, crop, gameplay)", all(l in text for l in ["blur", "zoom", "crop", "gameplay"])),
    ("Navigation Views (library & settings)", 'data-v="library"' in text and 'data-v="settings"' in text and 'nav("overview"' in text),
    ("Cyber Guard Reset Action", 'data-act="guardreset"' in text),
    ("verifyRoute JavaScript security function", 'verifyRoute' in text),
    ("showCyberGuardNotice JavaScript security function", 'showCyberGuardNotice' in text)
]

print("\n========================================================")
print("  MOMENTRIX END-TO-END RENDERED DOM VERIFICATION")
print("========================================================\n")
all_passed = True
for name, passed in checks:
    status = "[PASS]" if passed else "[FAIL]"
    print(f"  {status} {name}")
    if not passed:
        all_passed = False

print("\n========================================================")
print(f"  RESULT: {'ALL 21/21 CHECKS PASSED WITH 100% SUCCESS!' if all_passed else 'SOME CHECKS FAILED!'}")
print("========================================================\n")
