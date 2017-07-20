def problem2_7():
    print('enter length of side one:', end='')
    a = float(input())
    print('enter length of side two:', end='')
    b = float(input())
    print('enter length of side three:', end='')
    c = float(input())
    p = 0.5*(a+b+c)
#    print(peri)
    area = p*(p-a)*(p-b)*(p-c)
    area = area**(0.5)
    print('Area of a triangle with sides',a,b,c,'is',area)

#problem2_7()


