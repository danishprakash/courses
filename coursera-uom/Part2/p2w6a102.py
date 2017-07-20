name = raw_input('Enter the file name: ')
if len(name) < 1 : name = 'mbox-short.txt'
fh = open(name)

hours = {}
lst = list()

for line in fh:
    if not line.startswith("From "):
        continue
    email = line.split()
    hour = line[line.find(':')-2:line.find(':')]
    hours[hour] = hours.get(hour, 0) + 1

fnl = hours.items()
fnl.sort()
for item in fnl:
    print item[0], item[1]

fh.close()
