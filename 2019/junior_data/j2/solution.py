import sys

def solution(number):
    d = []
    out = []
    for i in range(1, int(number[0]) + 1):
        v = number[i].split(" ")
        v[1] = v[1][:-1]
        d.append(v)

    print(v)
    sym = []
    for i in range(0, len(d)):
        n = int(d[i][0])
        sym.append(d[i][1] * n)
    
    print(sym)
    return sym

in_file_name = sys.argv[1]
with open(in_file_name, 'r') as f:
    lines = f.readlines()
numbers = []
for i in range(len(lines)):
    numbers.append(lines[i])
result = solution(numbers)

out_file_name = '.'.join(in_file_name.split('.')[:-1]) + '.test'
with open(out_file_name, 'w') as f:
    for i in range(0, len(result)):
        f.write(result[i] + "\n")
