from cgi import test
import os, glob

test_cases = glob.glob('*.in')

for path in test_cases:
    with open(path) as f:
        lines = f.readlines()
    rules = [line.split() for line in lines[:3]]
    steps, cur, target = lines[-1].split()
    steps = int(steps)

    with open(path.replace('in', 'test')) as f:
        for _ in range(steps):
            line = f.readline()
            rid, pos, s = line.split()
            rid = int(rid) - 1
            pos = int(pos) - 1
            rule = rules[rid]
            assert cur[pos:pos+len(rule[0])] == rule[0]
            assert s[pos:pos+len(rule[1])] == rule[1]
            cur = s
        assert s == target

    print(f"{path}: PASSED")
