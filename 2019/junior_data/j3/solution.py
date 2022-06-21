import sys

def solution(number):
    encod = []
    for i in range(1, int(number[0]) +1):
        counter = 0
        string = ""   
        h = number[i]
        for j in range(len(h)):
            if j!=len(h)-1 and h[j] == h[j+1]:
                counter += 1
            else:
                string = string + " " + str(counter +1) + " " + h[j]
                msg = string[1:len(string) - 4]
                counter = 0
            
        encod.append(msg)
    
    print(encod)
    return encod

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
