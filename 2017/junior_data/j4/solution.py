import sys

def solution(number):
    a = int(number[0]) // 720 * 31
    b = int(number[0]) % 720
    out = 0
    hour = 12
    minute = 0 

    for i in range(b):
        minute += 1
        if minute == 60:
            minute = 0
            if hour == 12:
                hour = 1
            else:
                hour += 1
        l = list(str(hour))
        if minute < 10:
            l.append("0")
            l.append(str(minute))
        else:
            l.append(str(minute)[0])
            l.append(str(minute)[1])
    
        dif = 10
        s = True
        for j in range(len(l)):
            if dif == 10:
                dif = int(l[j]) - int(l[j +1])
            elif j != len(l) - 1:    
                if dif != int(l[j]) - int(l[j + 1]):
                    s = False
        if s == True:
            out += 1
            s = False


    return str(out + a)

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
