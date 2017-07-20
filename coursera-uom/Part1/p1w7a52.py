#largest = None
#smallest = None
numList = []
while True:
    try:
        num = input("Enter a number: ")
        if num == 'done':
            break
        numList.append(int(num))
        #print(num)
    except:
        print('Invalid input')
print("Maximum is", max(numList))
print("Minimum is", min(numList))
