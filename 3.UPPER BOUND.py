def fun (arr,n,targte):
    low = 0 
    high = n - 1 
    ans = n 
    while(low <= high):
        mid = (low+high) // 2
        if ( arr[mid] >  target):
            high = mid -1 
            ans = mid
        else :
            low = mid + 1
        return ans 
arr = [1,2,3,6,7,8,9,10,11,12]
target = 10
n = len(arr)
res = fun(arr,n,target)
print(res)
        