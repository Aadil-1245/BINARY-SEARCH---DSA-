# Find the Target in the Roatated Sorted Array 
def fun(arr,target,n):
    low = 0 
    high = n -1 
    while(low <= high):
        mid = (low+high)//2
        if (arr(low) == target ):
            return mid 
        if (arr[low] <= target and target <= arr[mid ]):
            high = mid -1 
        else:
            low = mid + 1
            if (arr[mid] <= target and target <= arr[high]):
                low = mid + 1
            else:
                high = mid -1 
    return -1 
        

