with open(r"E:\Momentrix Clip\dom.html", "r", encoding="utf-8") as f:
    text = f.read()

print("Length of dom.html:", len(text))
print("data-v='library' in dom.html:", 'data-v="library"' in text)
print("o_max in dom.html:", "o_max" in text)
print("Has <div id='app'>:", 'id="app"' in text)
import re
app_content = re.findall(r'<div id="app"[^>]*>(.*?)</div>', text, re.DOTALL)
if app_content:
    print("app content snippet:", app_content[0][:200])
else:
    print("no app div matched")

