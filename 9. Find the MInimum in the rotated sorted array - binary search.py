def fun (arr,n):
    low = 0 
    high = n -1 
    ans = float('inf')
    while(low <= high):
        mid = (low + high)//2
        if (arr[low] <= arr[mid]):
            ans = min (ans , arr[low])
            low =  mid + 1
        else : 
            ans = min (ans,arr[mid])
            high = mid -1 
    return ans 
arr =[5,6,1,2,3,4]
n = len(arr)
print(fun(arr,n))