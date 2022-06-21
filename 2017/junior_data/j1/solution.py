import sys

def solution(number):
    x = int(number[0])
    y = int(number[1])
    if x > 0 and y > 0:
        return "1"
    elif x > 0 and y < 0:
        return "4"
    elif x < 0 and y > 0:
        return "2"
    else:
        return "3"

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
