import sys

def solution(number):
    n = int(number[0])
    k = int(number[1])
    sum = n
    for i in range(int(number[1])):
        num = n * (10 ** k)
        sum += num
        k -= 1
    
    return str(sum)

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
