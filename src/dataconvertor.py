import os

fileobj = open(
    "..\\dataset\\articles.txt")

lines = []

for line in fileobj:
    lines.append(line.strip())

urls = []

fileobj = open(
    "..\\dataset\\Data.txt", encoding="utf8")

for line in fileobj:
    urls.append(line.strip())

# ===========================================================================================================================================
for title, url in zip(lines, urls):
    with open(os.path.join("..\dataset\VSM-test", str(title+'.txt')), 'w', encoding="utf8") as f:
        f.write("%s\n" % title)
        f.write("%s\n" % url)
