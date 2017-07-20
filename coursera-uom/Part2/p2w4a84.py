fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    newlst = line.split()
    for word in newlst:
        if word not in lst:
            lst.append(word)
print(sorted(lst))