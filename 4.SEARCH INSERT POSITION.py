# we can also follow the same approach as we did for the lower bound 
def fun( arr, n, target):
    low = 0 
    high = n -1 
    ans  = n 
    while(low <= high):
        mid = (low + high )// 2
        if (arr[mid]>target):
            high = mid -1 
            ans = mid 
        elif (arr[mid ] == target):
            return mid 
        else :
            low = mid + 1
    return ans 

arr =[ 1,2,4,5]
n = len(arr)
target = 5
print(fun(arr,n,target))