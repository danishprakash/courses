
def comma(samlist):
    newString = ''
    for name in samlist:
        if name == samlist[-1]:
            newString += 'and ' + samlist[-1]
            break
        newString += str(name) + ', '
    print(newString)
#spam = ['apples', 'bananas', 'tofu', 'cats']
#comma(spam)
