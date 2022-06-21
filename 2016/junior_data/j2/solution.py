import sys

def solution(number):
    print(number)
    p = []
    for i in range(len(number)):
        l = number[i].split()
        p.append(l)
    s = int(p[i][0]) + int(p[i][1]) + int(p[i][2]) + int(p[i][3])
    s2 = 0
    s3 = 0
    for i in range(len(p) - 1):
        for j in range(len(p) - 1):
            s2 = int(p[i][0]) + int(p[i][1]) + int(p[i][2]) + int(p[i][3])
            s3 = int(p[0][j]) + int(p[1][j]) + int(p[2][j]) + int(p[3][j])
            if s != s2:
                return "not magic"
            if s != s3:
                return "not magic"
    
    return "magic"

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
