import sys

def solution(number):
    distances = number[0].split()
    print(distances)
    out = []
    f = [0]
    s = 0
    for i in range(1, 5):
        s += int(distances[i -1])
        f.append(s)

    line1 = "0"
    for i in range(1, len(f)):
        if i == 1:
            line1 += f" {f[i]} "
        else:    
            line1 += f"{f[i]} "
    out.append(line1)

    k = 1
    while k < 5:
        cur = f[k]
        for i in range(len(f)):
            if i < k:
                f[i] += cur
            else:
                f[i] -= cur
        line1 = ""
        for i in range(len(f)):
            if i < len(f):
                line1 += f"{f[i]} "
            elif i == len(f):
                line1 += f"{f[i]}"
        out.append(line1)
        k += 1

    return(out)

in_file_name = sys.argv[1]
with open(in_file_name, 'r') as f:
    lines = f.readlines()
numbers = []
for i in range(len(lines)):
    numbers.append(lines[i])
result = solution(numbers)

out_file_name = '.'.join(in_file_name.split('.')[:-1]) + '.test'
with open(out_file_name, 'w') as f:
    for i in result:
        f.write(i + "\n")
