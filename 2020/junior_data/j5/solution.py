import sys
from collections import deque

def solution(x, y, grid):
    d = {}
    for i in range(0, x):
        for j in range(0, y):
            key = (i + 1) * (j + 1)
            if key not in d:
                d[key] = []
            d[key].append([i+1, j+1])
    
    visited = set()
    q = deque()
    q.append([1,1])
    while len(q) > 0:
        a, b = q.popleft()
        # print(a, b)
        if a == x and b == y:
            return "yes"
        if grid[a-1][b-1] in visited:
            continue 
        if grid[a-1][b-1] not in d:
            continue
        for i in d[grid[a-1][b-1]]:
            visited.add(grid[a-1][b-1])
            q.append(i)
    return "no"

in_file_name = sys.argv[1]
with open(in_file_name, 'r') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
grid= []
for i in range(2, len(lines)):
    if len(lines[i]) > 0:
        f = lines[i].split(" ")
        f = [int(x) for x in f]
        grid.append(f)
result = solution(int(lines[0]), int(lines[1]), grid)

out_file_name = '.'.join(in_file_name.split('.')[:-1]) + '.test'
with open(out_file_name, 'w') as f:
    f.write(result + "\n")

        