import sys

def solution(number):
    wins = 0
    for i in number:
        if i == "W\n":
            wins += 1       

    if wins == 5 or wins == 6:
        return "1"
    elif wins == 3 or wins == 4:
        return "2"
    elif wins == 1 or wins == 2:  
        return "3"
    else:
        return "-1"


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
