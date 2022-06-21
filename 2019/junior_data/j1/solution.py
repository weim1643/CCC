import sys

def solution(number):
    a3 = int(number[0])
    a2 = int(number[1])
    a1 = int(number[2])
    b3 = int(number[3])
    b2 = int(number[4])
    b1 = int(number[5])

    ta = a3 * 3 + a2 * 2 + a1 * 1
    tb = b3 * 3 + b2 * 2 + b1 * 1

    if ta > tb:
        return "A"
    elif ta < tb:
        return "B"
    elif ta == tb:
        return "T"

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
