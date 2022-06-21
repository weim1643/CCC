import sys

def solution(number):
    str_1 = number[1]
    str_2 = number[2]
    count = 0
    for i in range(len(str_1) - 1):
        if str_1[i] == str_2[i] and str_1[i] != ".":
            count += 1

    return count


in_file_name = sys.argv[1]
with open(in_file_name, 'r') as f:
    lines = f.readlines()
numbers = []
for i in range(len(lines)):
    numbers.append(lines[i])
result = solution(numbers)

out_file_name = '.'.join(in_file_name.split('.')[:-1]) + '.test'
with open(out_file_name, 'w') as f:
    f.write(str(result) + "\n")
