import sys
line = sys.stdin.readline()
sq, rect, other = 0, 0, 0
while line:
    otherFound = False
    #line=line[:-1] if line[-1] == '\n' else line
    sides = line.split()
    sides = [int(s) for s in sides]

    for s1 in sides:
        if s1 <= 0:
            otherFound = True
            other += 1
            break
    if not otherFound:
        if sides[0]==sides[1]==sides[2]==sides[3]:
            sq += 1
        elif sides[0]==sides[2] and sides[1]==sides[3]:
            rect += 1
        else:
            other += 1
    line = sys.stdin.readline()
print sq, rect, other

***********************************
import sys
words = sys.stdin.readline()
M = int(raw_input())
mydict = {}
for _ in range(2*M):
    id = int(raw_input())
    count = 0
    review = sys.stdin.readline()
    review = line[:-1] if line[-1] == '\n' else review
    review = review.split()
    review = [r.strip(",.") for r in review]
    for wr in review:
        if wr in words:
            count+=1
    mydict[id] = mydict.get(id, 0) + count

import operator
sorted_x = sorted(mydict.items(), key=operator.itemgetter(1), reverse=True)
for sx in sorted_x:
    sys.stdout.write(sx[0])
sys.stdout.flush()

import sys
numbers = sys.stdin.readline()
numbers = numbers[-1]
numbers = numbers.split()
numbers = [int(n) for n in numbers]
result = [numbers[0]]
prev = numbers[0]
for x in numbers[1:]:
    diff = x - prev
    if diff > 127 or diff < -127:
        result.append(-128)
    result.append(diff)
    prev = x
for r in result:
    print r,

S = int(raw_input())
M = int(raw_input())
mydict = {}
found = False
for _ in range(M):
    x = int(raw_input())
    if S-x in mydict:
        found = True
    mydict[x] = 1
if found:
    print 1
else:
    print 0





