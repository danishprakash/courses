name = raw_input("Enter the filename: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lst = list()
seclst = list()

for line in handle:
    if not line.startswith("From: "): continue
    lst = line.split()
    seclst.append(lst[1])
print(max(lst) + ' ' + str(seclst.count(max(lst))))

handle.close()
