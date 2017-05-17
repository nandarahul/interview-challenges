
import sys
IE = "INVALID EXPRESSION"
# Expression will be a list
# This function will return a number
def create_expression(mlist):
    while '*' in mlist:
        pos = mlist.index('*')
        mlist = mlist[:pos-1] + [mlist[pos-1:pos+2]] + mlist[pos+2:]
    return mlist


def evaluate(expression):
    if len(expression) == 1:
        try:
            return int(expression[0])
        except:
            return IE
    if len(expression) == 3:
        if expression[1] == '*':
            return evaluate(expression[0]) * evaluate(expression[2])
        if expression[1] == '+':
            return evaluate(expression[0]) + evaluate(expression[2])
        if expression[1] == '-':
            return evaluate(expression[0]) - evaluate(expression[2])
        if expression[1] == '/':
            return evaluate(expression[0]) / evaluate(expression[2])


line = sys.stdin.readline()
lines = []
while line:
    line = line[:-1]
    line = [l.strip() for l in line.split(',')]
    lines.append(line)
    line = sys.stdin.readline()

if '_' in lines[0] or '_' in lines[-1] or len(lines) %2 ==0:
    print IE
    sys.exit()

if len(lines) == 1:
    exp = create_expression(lines[0])
    print evaluate(exp)

else:
    ex = []
    for l, i in enumerate(lines):
        if i %2 :
            l[]
        create_expression()



