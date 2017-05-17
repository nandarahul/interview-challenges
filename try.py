import sys

def method1():
    x = sys.stdin.readlines()
    for l in x:
        print l[:-1]

def method2():
    line = sys.stdin.readline()
    while line:
        line=line[:-1] if line[-1] == '\n' else line
        print line
        line = sys.stdin.readline()
    if not line:
        print "ehh"
    print type(line)

def check_valid_hour(hour):
    return 0 <= hour <= 23

def check_valid_minute(minute):
    return 0 <= minute <= 59

def traverse(arr, preOrder):
    if not arr:
        return
    min_index = arr.index(min(arr))
    preOrder.append(arr[min_index])
    traverse(arr[:min_index], preOrder)
    traverse(arr[min_index+1:], preOrder)

def  getPreOrder(arr):
    preOrder = []
    traverse(arr, preOrder)
    return preOrder

if __name__ == "__main__":
    print getPreOrder([8,2,7,1,9,3,20])


def solution(A, B, C, D):
    # write your code in Python 2.7
    numbers = [A, B, C, D]
    two_digits = []
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            if i == j:
                continue
            two_digits.append(x*10 + y)
    two_digits.sort(reverse=True)
    two_digits = ['0'+str(tg) if tg < 10 else str(tg) for tg in two_digits]
    numbers = [str(n) for n in numbers]
    print numbers
    for x in two_digits:
        if check_valid_hour(int(x)):
            for y in two_digits:
                ncopy = numbers[:]
                ncopy.remove(x[0])
                ncopy.remove(x[1])
                if y[0] in ncopy and y[1] in ncopy and check_valid_minute(int(y)):
                    hour, minute = x, y
                    return hour+":"+minute
    return "NOT POSSIBLE"

#print solution(4,0,0,2)


