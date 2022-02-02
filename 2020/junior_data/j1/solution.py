import sys

def solution(number):
    total = int(number[0]) * 1 + int(number[1]) * 2 + int(number[2]) * 3
    if total >= 10:
        return "happy"
    else:
        return "sad"

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
        f.write(i)
