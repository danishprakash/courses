#merge sort

def merge_sort(a, p, r):
    if p < r:
        q = (p+r)//2 
        merge_sort(a,p,q)
        merge_sort(a,q+1,r)
        merge(a,p,q,r)

def merge(a,p,q,r): 
    n1 = p-q+1
    n2 = r-q
    l1 = a[p:q+1]
    l2 = a[q+1:r+1]
    l1.append(55555)        #arbitrarily large number to check end of list
    l2.append(55555)
    j,k = [0,0]
    for l in range(p,r+1):
        if l1[j] <= l2[k]:
            a[l] = l1[j]
            j += 1
        else: 
            a[l] = l2[k]
            k += 1 

a = [int(x) for x in input().split()]
merge_sort(a, 0, len(a)-1)
a = [str(s) for s in a]
print(' '.join(a))
