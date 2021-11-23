import os

fileobj = open(
    "C:\\KR\\IR\\Test\\PageRank-HITS-SimRank\\dataset\\articles.txt")
lines = []
for line in fileobj:
    lines.append(line.strip())

for item in lines:
    with open(os.path.join("C:\KR\IR\Test\PageRank-HITS-SimRank\dataset\VSM", str(item+'.txt')), 'w') as f:
        f.write("%s\n" % item)
