import sys

infile = open(sys.argv[1])
outfile = open(sys.argv[2], 'w')

for line in infile:
    line = line.strip('\n')
    line_length = len(line)
    outfile.write(str(line_length)+'\n')

outfile.close()
infile.close()

