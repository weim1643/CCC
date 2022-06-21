import sys

def solution(number):
    n1 = int(number[0])
    n2 = int(number[1])
    n3 = int(number[2])
    n4 = int(number[3])
    if n1 >= 8 and n4 >= 8 and n3 == n2:
        return "ignore"
    else:
        return "answer"

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
        if pp < 5:
            f.write(i)
        else:
            f.write(i + "\n")
        pp += 1
