hrs = float(input("Enter Hours:"))
rph = float(input("Enter rate per hours: "))
if hrs > 40:
    ovt = hrs - 40
    hrs = hrs - ovt
    gpa = hrs * rph
    gpa += ovt * 1.5 * rph
print (gpa)
