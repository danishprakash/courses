score = float(input("Enter Score: "))
#if score in float(range(0,1))
if score > 1:
    print ('Error')
elif score >= 0.9:
    print ('A')
elif score >= 0.8:
    print ('B')
elif score >=  0.7:
    print ('C')
elif score >= 0.6:
    print ('D')
elif score < 0.6:
    print ('F')
elif score < 0:
    print ('Error')
