import sys

def solution(number):
    t = [1,2,3,4]
    for i in range(len(number)):
        if number[i] == "V":
            j = t[0]
            t[0] = t[1]
            t[1] = j
            k = t[2]
            t[2] = t[3]
            t[3] = k
        elif number[i] == "H":
            j = t[0]
            t[0] = t[2]
            t[2] = j
            k = t[1]
            t[1] = t[3]
            t[3] = k
    print(t)
    out = []
    for i in range(0, len(t), 2):
        out.append(str(t[i]) + " " + str(t[i + 1]))

    print(out)
    return out    

in_file_name = sys.argv[1]
with open(in_file_name, 'r') as f:
    lines = f.readlines()
numbers = ""
for i in range(len(lines)):
    numbers = lines[i]
result = solution(numbers)

out_file_name = '.'.join(in_file_name.split('.')[:-1]) + '.test'
with open(out_file_name, 'w') as f:
    for i in result:
        f.write(i + "\n")