from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
print(d)
for k, v in s:
    d[k].append(v)

print(sorted(d.items()))
