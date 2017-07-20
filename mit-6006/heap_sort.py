def max_heapify(a, i):
    #print(a)
    l = 2*(i+1)
    r = (2*(i+1)) + 1
    #print(l, i, r) 
    if l <= len(a) and a[l-1] > a[i]:
        largest = l
    else:
        largest = i+1
    if r <= len(a) and a[r-1] > a[largest-1]:
        largest = r
    #print("largest: ", str(largest))

    if largest != i+1:
        temp = a[largest-1]
        a[largest-1] = a[i]
        a[i] = temp
        max_heapify(a, largest-1)

def build_max_heap(a):
    n = len(a)
    for i in range((n//2)-1, -1, -1):
        max_heapify(a, i)

a = [int(x) for x in input().split()]
build_max_heap(a)
a = [str(x) for x in a]
print(' '.join(a))
