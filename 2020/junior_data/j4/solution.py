import sys

def solution(s1, s2):
    fe = []
    for i in range(0, len(s2)):
        fe.append(s2[i:] + s2[:i])
    for i in range(0, len(fe)):
        if fe[i] in s1:
            return "yes"
    return "no"
    
in_file_name = sys.argv[1]
with open(in_file_name, 'r') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
result = solution(lines[0], lines[1])

out_file_name = '.'.join(in_file_name.split('.')[:-1]) + '.test'
with open(out_file_name, 'w') as f:
    f.write(result + "\n")

        