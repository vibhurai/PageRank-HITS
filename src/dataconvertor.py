import os
import csv
fileobj = open(
    "..\\dataset\\articles.txt")
lines = []
for line in fileobj:
    lines.append(line.strip())

# my_list = []
# with open('..\\dataset\\Data.csv', 'r') as f:
#     print()
#     # file = csv.reader(f)
#     # my_list = list(file)
# print(lines)
# fileobj = open(
#     "C:\\KR\\IR\\Test\\PageRank-HITS-SimRank\\dataset\\Data.csv")
# liness = []
# for line in fileobj:
#     lines.append(line.strip())

# print(liness)

for item in lines:
    with open(os.path.join("C:\KR\IR\Test\PageRank-HITS-SimRank\dataset\VSM", str(item+'.txt')), 'w') as f:
        f.write("%s\n" % item)
#         f.write("%s\n" % item)
