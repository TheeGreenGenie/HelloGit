import sys
import string

SHIFT = sys.argv[1]
line_p = ''

for line in sys.stdin:
    for i in line:
        if i in string.ascii_letters:
            line_p+=i

def encoder(shift, txt):
    rtrn=''
    uppercase = string.ascii_uppercase
    one26 = [i+1 for i in range(26)]
    one26v2 = one26[shift:]+one26[:shift]
    normal = {i:x for (i,x) in zip(one26,uppercase)}
    pushed = {i:x for (i,x) in zip(uppercase,one26v2)}
    count=0
    for i in txt:
        if i in string.ascii_letters:
            if count % 5==0 and count != 0:
                rtrn+=' '
            index_pushed = pushed[i.upper()]
            letter = normal[index_pushed]
            rtrn+=letter
            count+=1
        else:
            pass
    return rtrn

print(encoder(int(SHIFT), line_p))
