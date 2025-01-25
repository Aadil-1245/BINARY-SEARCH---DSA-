# Find the targte in the roatted sorted array which has the duplicates 
def fun (arr,target,n):
    low = 0 
    high = n-1 
    while(low<=high):
        mid = (low+high)//2
        if (arr[mid] == target ):
            return mid 
        if(arr[low] == arr[mid] and arr[mid] == arr[high]):
            low = low +1 
            high = high -1 
        elif(arr[low] <= arr[mid]):
            if(arr[low] <= target and target < arr[mid]):
                high = mid -1 
            else:
                low = mid +1 
        else:
            if (arr[mid] <= target < arr[high]):
                low = mid =1 
            else:
                high = mid -1 
    return -1 


arr = [7,8,9,1,2,3,4,5,6]
target = 1
n = len(arr)
print(fun(arr,target,n))





