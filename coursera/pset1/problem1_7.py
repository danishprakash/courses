def problem1_7():
    print ('Enter the length of one of the bases: ', end=" ")
    l = float(input())
    print ('Enter the length of the other base: ',end=" ")
    l2 = float(input())
    print ('Enter the height: ',end=" ")
    h =float(input())
    area = (l+l2)*(1/2)*h
    print ('The area of a trapezoid with bases ' + str(l) + ' and ' + str(l2) +
            ' and height ' + str(h) + ' is ' + str(area))

#problem1_7()
