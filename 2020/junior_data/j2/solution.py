import sys

def solution(number):
    n = int(number[1])
    c = 0
    i = n
    while i <= int(number[0]):
        i += n * int(number[2])
        n = n * int(number[2])
        c += 1
    return str(c)

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
