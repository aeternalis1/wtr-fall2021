infile = open("data/train_set.txt", "r")

cnt = 0
lines = set()
for line in infile.readlines():
    lines.add(line.strip())
print (len(lines))