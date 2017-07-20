#s = 'azcbobobegghakl'
s = 'abcdefghijklmnopqrstuvwxyz'
lst = [s[0]]
mlst = list()
for i in range(1,len(s)):
    #print(s[i])
    if s[i] >= lst[-1]:
        lst.append(s[i])
    else:
        mlst.append(lst)
        lst = [s[i]]
mlst.append(lst)
#print(''.join(lst))
if len(mlst) <= 1:
    print(''.join(mlst[0]))
else:
    print(''.join(max(mlst, key=len)))
#print(mlst)
