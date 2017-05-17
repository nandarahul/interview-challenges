def reverse_special(mystrr):
    mystr = list(mystrr)
    print mystr
    i, j = 0, len(mystr)-1
    while i < j:
        special = False
        if mystr[i].lower() < 'a' or mystr[i].lower() > 'z':
            i += 1
            special = True
        if mystr[j].lower() < 'a' or mystr[j].lower() > 'z':
            j -= 1
            special = True
        if not special:
            mystr[i], mystr[j] = mystr[j], mystr[i]
            i += 1
            j -= 1
    mystrr = ''.join(s for s in mystr)
    return mystrr

count = 0
def permute(mystr, pos):
    if isinstance(mystr, str):
        mystr = list(mystr)
    for i in range(pos, len(mystr)):
        newstr = mystr
        newstr[i], newstr[pos] = newstr[pos], newstr[i]
        permute(newstr, pos+1)
        newstr[i], newstr[pos] = newstr[pos], newstr[i]

    if pos == len(mystr) - 1:
        global count
        count += 1
        print ''.join(mystr)

def test(k):
    k[0] = 11111

if __name__ == "__main__":
    #print reverse_special("Ab,c,de!$")
    #permute('rahul', 0)
    #print count
    #k = [1,2]
    k = 5
    test(k)
    print k


