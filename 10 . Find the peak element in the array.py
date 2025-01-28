# Find the peak element in the array 
def fun (arr,n):
    low = 0 
    high = n -1 
    if (n == 1 ):
        return n 
    if (arr[0] > arr[1]):
        return arr[0]
    if (arr[n-1 ] > arr[n-2 ]):
        return arr[n-1 ]
    low = low +1 
    high = high - 1
    while(low <= high):
        mid = (low +high)//2
        if (arr[mid-1] < arr[mid] > arr[mid +1 ]):
            return arr[mid ]
        if (arr[mid -1 ] > arr[mid] > arr[mid +1 ]):
            high = mid -1 
        else :
            low = mid +1 


    return 1 
arr = [ 1,8,9,10,3,4,2]
n = len(arr)
print(fun(arr,n))