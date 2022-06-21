import sys

def solution(rules, steps, cur, target, max_reduce):
    if steps == 0:
        if cur == target:
            return []
        else:
            return None

    if len(cur) - len(target) > steps * max_reduce:
        return None
    
    for i, (k, v) in enumerate(rules):
        for o in range(len(cur) - len(k) + 1):
            l = 0
            while l < len(k):
                if cur[o+l] != k[l]:
                    break
                l += 1
            if l == len(k):
                next = cur[:o] + v + cur[o+l:]
                result = solution(rules, steps - 1, next, target, max_reduce)
                if result != None:
                    result.append((i+1, o+1, next))
                    return result

    return None

in_file_name = sys.argv[1]
with open(in_file_name, 'r') as f:
    lines = f.readlines()

rules = [line.split() for line in lines[:3]]

max_reduce = max([len(l) - len(r) for l, r in rules])
max_reduce = max(max_reduce, 0)

steps, cur, target = lines[-1].split()
steps = int(steps)

result = solution(rules, steps, cur, target, max_reduce)

out_file_name = '.'.join(in_file_name.split('.')[:-1]) + '.test'

with open(out_file_name, 'w') as f:
    for t in reversed(result):
        f.write(" ".join(map(str, t)) + "\n")
