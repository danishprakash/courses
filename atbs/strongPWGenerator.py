import re

password = input()
pwregex = re.compile(r'([a-z]+[A-Z]+[0-9]+){8:}')
mo = pwregex.search('wA1wA1wA1wA1wA1wA1wA1wA1')
if mo == None:
    print('NULL')
else:
    print(mo.group[0])
