

def print_encoding(str, encoding):
    if len(encoding) == 0:
        print str
        return
    if not int(encoding[0]):
        print "INVALID Encoding"
        return
    if len(encoding) >= 2:
        if encoding[1] == '0':
            if int(encoding[:2]) > 26:
                print "Invalid Encoding"
                return
            print_encoding(str+chr(96+int(encoding[:2])), encoding[2:])
            return
        if int(encoding[:2]) <= 26:
            print_encoding(str+chr(96+int(encoding[:2])), encoding[2:])
    print_encoding(str+chr(96+int(encoding[0])), encoding[1:])

print_encoding("", '4140111')



