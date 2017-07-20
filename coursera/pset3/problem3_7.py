import csv
def problem3_7(csv_pricefile, flower):
    rfile = open(csv_pricefile)
    for item in csv.reader(rfile):
        if item[0] == flower:
            print(item[1])
            break
        #print(item)    
    rfile.close()
#problem3_7("flowers.csv", "alyssum")
