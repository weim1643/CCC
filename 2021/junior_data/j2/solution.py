import sys

def solution(bid, names):
    maxi = -1
    d = ""
    for i in range(0, len(bid)):
        if bid[i] > maxi:
            maxi = bid[i]
            d = names[i]
    return d

in_file_name = sys.argv[1]
with open(in_file_name, 'r') as f:
    lines = f.readlines()
N = int(lines[0])
lines = lines[1:]
bids = []
names = []
for i in range(N):
    names.append(lines[i*2])
    bids.append(int(lines[i*2+1]))
result = solution(bids, names)

out_file_name = '.'.join(in_file_name.split('.')[:-1]) + '.test'
with open(out_file_name, 'w') as f:
    f.write(result)
