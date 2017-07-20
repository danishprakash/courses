# Paste your code into this box 
s = input()
counter = 0
for i in range(len(s)):
    #print(i)
    if s[i:i+3] == 'bob':
        counter += 1
print(counter)
