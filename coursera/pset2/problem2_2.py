def problem2_2(samlist):
    l =[]
    print(samlist)
    print(samlist[0])
    print(samlist[len(samlist)-1])
    for num in range(3, 5):
        l.append(samlist[num])
    print(l)
    l = []
    for num in range(0,3):
       l.append(samlist[num])
    print(l)
    l = []
    for num in range(3,len(samlist)):
        l.append(samlist[num])
    print(l)
    print(len(samlist))
    samlist.append("z")
    print(samlist)

#alist = ["a","e","i","o","u","y"]
#blist = ["alpha", "beta", "gamma", "delta", "epsilon", "eta", "theta"]
#problem2_2(blist)
