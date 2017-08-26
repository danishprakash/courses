# http://www.geeksforgeeks.org/radix-sort/

# Implementation of Radix Sort using Counting Sort as a subroutine

def counting_sort(a, exp):
    b = [0 for x in range(len(a))]
    c = [0 for x in range(10)]
    for i in range(len(a)):
        index = a[i]//exp
        c[index%10] += 1

    for i in range(1, len(c)):
        c[i] += c[i-1]
    for i in range(len(b)):
        index = a[i]//exp
        b[c[index%10]-1] = a[i]
        c[index%10] -= 1
    
    for i in range(len(a)):
        a[i] = b[i]

def radix_sort(a):
    maxl = max(a)
    exp = 1

    while maxl//exp > 0:
        counting_sort(a, exp)
        exp *= 10

a = [int(x) for x in input().split()]
radix_sort(a)
print(' '.join([str(x) for x in a]))
