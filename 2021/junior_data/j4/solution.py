import sys

def solution(books):
    d = {"L": 0, "M": 0, "S": 0}
    for i in books:
        d[i] += 1
    
    l_in_m = 0
    s_in_m = 0
    for i in range(d['L'], d['L'] + d["M"]):
        if books[i] == "L":
            l_in_m += 1
        elif books[i] == "S":
            s_in_m += 1
    
    m_in_s = 0
    l_in_s = 0
    for i in range(d['M'] + d["L"], len(books)):
        if books[i] == "L":
            l_in_s += 1
        elif books[i] == "M":
            m_in_s += 1

    count = 0
    for i in range(0, d["L"]):
        if books[i] == "S":
            if l_in_s > 0:
                count += 1
                l_in_s -= 1
            else:
                count += 2
                l_in_m -= 1
                m_in_s -= 1
        elif books[i] == "M":
            if l_in_m > 0:
                count += 1
                l_in_m -= 1
            else:
                count += 2
                s_in_m -= 1
                l_in_s -= 1
 
    return count + m_in_s

in_file_name = sys.argv[1]
with open(in_file_name, 'r') as f:
    lines = f.readlines()
books = lines[0].strip()
result = solution(books)

out_file_name = '.'.join(in_file_name.split('.')[:-1]) + '.test'
with open(out_file_name, 'w') as f:
    f.write(str(result) + "\n")
