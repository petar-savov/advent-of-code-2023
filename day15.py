from collections import defaultdict

with open("input-15.txt") as f:
    data = [x.strip() for x in f.read().split(",")]


def do_hash(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h


print(sum(do_hash(s) for s in data))

boxes = defaultdict(dict)

for cmd in data:
    if "-" in cmd:
        label = cmd[:-1]
        boxes[do_hash(label)].pop(label, None)
    else:
        label, i = cmd.split("=")
        boxes[do_hash(label)][label] = int(i)

print(sum((i + 1) * (j + 1) * k for i in boxes for j, k in enumerate(boxes[i].values())))
