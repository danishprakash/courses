# Use the file name mbox-short.txt as the file name
bum = 0;
counter = 0
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else: 
        bum += float(line[line.find("0"):]) 
        counter += 1
    #print line
#print "Done"
avg = bum/counter
print("Average spam confidence: " + str(avg))
