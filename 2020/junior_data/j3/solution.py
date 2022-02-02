import sys

def solution(number):
    maxx = -1
    maxy = -1
    minx = 101
    miny = 101
    l = []

    for i in range(1, int(number[0]) +1):
        l.append(number[i].split(","))
    # print(l)
    # print(number)

    for i in range(0, len(l)):
        maxx = max(maxx, int(l[i][0]))
        maxy = max(maxy, int(l[i][1]))
        minx = min(minx, int(l[i][0]))
        miny = min(miny, int(l[i][1]))
    
    maxx += 1
    maxy += 1
    minx -= 1
    miny -= 1

    o = f"{minx},{miny}"
    k = f"{maxx},{maxy}"

    out = [o, k]
    return out

in_file_name = sys.argv[1]
with open(in_file_name, 'r') as f:
    lines = f.readlines()
numbers = []
for i in range(len(lines)):
    numbers.append(lines[i])
result = solution(numbers)

pp = 0
out_file_name = '.'.join(in_file_name.split('.')[:-1]) + '.test'
with open(out_file_name, 'w') as f:
    for i in result:
        if pp < 1:
            f.write(i + "\n")
        else:
            f.write(i)
        pp += 1
        