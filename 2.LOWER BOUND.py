def fun (arr,n,target):
    low = 0 
    high = n - 1
    ans = n
    while (low <= high):
        mid = (low+high) // 2
        if (arr[mid]>target):
            high = mid -1 
            ans = mid 
        else:
            low = mid +1 
    return ans 
arr = [ 1,2,4,5,6,8,9]
target = 3
n = len(arr)
res = fun(arr,n,target)
print(res)