#binary insertion sort
def binary_search(a, k, i):
    beg = 0
    end = len(a)-1 
    while True:
        mid = (beg + end) // 2
        if end <= beg:
            if k > a[beg]: 
                return beg+1
            else:
                return beg 
        elif k < a[mid]:
            if mid-1 < 0:
                return 0
            else:
                end = mid-1
        elif k >= a[mid]:
                beg = mid+1
    return i

def insertion_sort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        b = a[:j+1] 
        pos = binary_search(b,key, i)
        while j >= pos:
            a[j+1] = a[j]
            j -= 1
        a[pos] = key
    a = [str(x) for x in a]
    return ' '.join(a)

a = [int(x) for x in input().split()]
print(insertion_sort(a))

