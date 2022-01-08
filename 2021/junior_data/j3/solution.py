import sys

def solution(number):
    direct = []
    steps = []
    r = []
    for i in range(0, len(number)):
        if int(number[i]) == 99999:
            break
        x = int(number[i][0]) + int(number[i][1])
        if x == 0:
            direct.append(direct[-1])
        elif x % 2 == 0:
            direct.append("right")
        elif x % 2 == 1:
            direct.append("left")
        
        steps.append(str(number[i][2:5]))
    for i in range(0, len(direct)):
        r.append(f"{direct[i]} {steps[i]}")
    return r

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
