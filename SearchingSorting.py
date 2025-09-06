# 31. Linear Search
def linear_search(arr, x):
    for i, val in enumerate(arr):
        if val == x: return i
    return -1

# 32. Binary Search
def binary_search(arr, x):
    l, r = 0, len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==x: return mid
        elif arr[mid]<x: l=mid+1
        else: r=mid-1
    return -1

# 33. Bubble Sort
arr=[5,1,4,2]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

# 34. Selection Sort
arr=[64,25,12,22,11]
for i in range(len(arr)):
    min_idx=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_idx]: min_idx=j
    arr[i],arr[min_idx]=arr[min_idx],arr[i]
print(arr)

# 35. Insertion Sort
arr=[12,11,13,5,6]
for i in range(1,len(arr)):
    key=arr[i]; j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]; j-=1
    arr[j+1]=key
print(arr)

# 36. Quick Sort
def quicksort(arr):
    if len(arr)<=1: return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    mid=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quicksort(left)+mid+quicksort(right)
print(quicksort([3,6,8,10,1,2,1]))

# 37. Merge Sort
def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]; R=arr[mid:]
        merge_sort(L); merge_sort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]: arr[k]=L[i]; i+=1
            else: arr[k]=R[j]; j+=1
            k+=1
        arr[k:]=L[i:]+R[j:]
    return arr
print(merge_sort([38,27,43,3,9,82,10]))

# 38. Count Sort
def count_sort(arr):
    max_val=max(arr); m=max_val+1
    count=[0]*m
    for a in arr: count[a]+=1
    result=[]
    for i in range(m):
        result+= [i]*count[i]
    return result
print(count_sort([4,2,2,8,3,3,1]))

# 39. Heap Sort
import heapq
arr=[3,1,4,1,5,9]
heapq.heapify(arr)
print([heapq.heappop(arr) for _ in range(len(arr))])

# 40. Kth smallest element
arr=[7,10,4,3,20,15]; k=3
print(sorted(arr)[k-1])
