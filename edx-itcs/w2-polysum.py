import math

def polysum(n, s):
    peri = n*s
    area = ((0.25*n*s*s)/math.tan(math.pi/n))
    return round((area+(peri*peri)), 4)
	
sides = float(raw_input("Enter the no. of sides of the polygon: "))
length = float(raw_input("Enter the lenght of the side of the polygon: "))
#print("{0:.2f}".format((polysum(sides, lenght)))
print(polysum(sides, length))
