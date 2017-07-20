def computepay(h,r):
    global hrs
    if hrs > 40:
    	ovt = hrs - 40
    	hrs = hrs - ovt
    	gpa = hrs * rph
    	gpa += ovt * 1.5 * rph
    return gpa

hrs = float(input("Enter Hours:"))
rph = float(input("Enter Rate per hour: "))
p = computepay(hrs,rph)
print(p)