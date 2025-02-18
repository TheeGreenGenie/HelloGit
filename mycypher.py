import sys
import string


def doSomething(var):
    rtrn = ''
    uppercase = string.ascii_uppercase
    one26 = [i+1 for i in range(26)]
    one26v2 = one26[3:]+one26[:3]
    normal = {i:x for (i,x) in zip(one26,uppercase)}
    pushed = {i:x for (i,x) in zip(uppercase,one26v2)}
    for i in var:
        count=0
        if i in string.ascii_letters:
            count+=1
            index_pushed = pushed[i.upper()]
            letter = normal[index_pushed]
            rtrn+=letter
        else:
            pass
    return rtrn

example = """AAABBBCCCILIKEDOGS
CCCDDDEEEilikedogs
ooopppqqqilikedogs
mmm888666uuugggilikedogs
"""
result =''
for line in example:
    result+=doSomething(line)
updated_results=""
for i, x in enumerate(result):
    if i%5==0 and i!=0:
        updated_results+=" "
    updated_results+=x

print(updated_results)