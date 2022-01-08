import sys

def solution(boiling_point: int):
    P = 5 * boiling_point - 400
    if P < 100:
        return (P, 1)
    elif P == 100:
        return(P, 0)
    else:
        return(P, -1)

in_file_name = sys.argv[1]
with open(in_file_name, 'r') as f:
    lines = f.readlines()
result = solution(int(lines[0]))

out_file_name = '.'.join(in_file_name.split('.')[:-1]) + '.test'
with open(out_file_name, 'w') as f:
    for v in result:
        f.write(str(v) + '\n')
