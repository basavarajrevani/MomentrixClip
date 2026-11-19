import re

with open(r"E:\Momentrix Clip\dom.html", "r", encoding="utf-8") as f:
    text = f.read()

print("9:16:", "9:16" in text)
print("16:9:", "16:9" in text)
print("aspect matches:", re.findall(r'aspect[^"\'<>\s]*', text)[:5])
print("data-v matches:", re.findall(r'data-v="[^"]+"', text)[:10])
print("nav matches:", re.findall(r'nav\("[^"]+"', text)[:10])

