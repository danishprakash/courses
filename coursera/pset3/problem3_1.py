counter = 0
line_counter = 0
def problem3_1(txtfilename):
    global counter 
    global line_counter
    infile = open(txtfilename)
    for line in infile:
        print(line, end="")
        counter += len(line)
        line_counter += 1
    if line_counter < 1:
        counter -= 1
    print('\nThere are ' + str(counter-1)+ ' letters in the file.\n')
    #print(line_counter)
#problem3_1("sample.txt")
