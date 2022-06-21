import sys

def solution(number):
    x1, y1 = number[0].split()
    x2, y2 = number[1].split()
    num = int(number[2])

    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    j = abs(x1 - x2) + abs(y1 - y2)
    if num >= j and (num - j) % 2 == 0:
        return "Y"
    else:
        return "N"


in_file_name = sys.argv[1]
with open(in_file_name, 'r') as f:
    lines = f.readlines()
numbers = []
for i in range(len(lines)):
    numbers.append(lines[i])
result = solution(numbers)

out_file_name = '.'.join(in_file_name.split('.')[:-1]) + '.test'
with open(out_file_name, 'w') as f:
    f.write(result + "\n")
