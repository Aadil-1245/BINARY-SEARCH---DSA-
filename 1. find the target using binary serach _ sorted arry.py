#ITERATIVE METHOD OF SOLVING 
def fun(arr,n,target):
    low = 0 
    n = len(arr)
    high = n -1 
    while(low <= high):
        mid = low + high // 2 
        if (arr[mid] == target):
            return mid
        elif(target > arr[mid]):
            low = mid +1 
        else:
            high = mid -1 
        return -1 
arr = [ -1 , 2, 5, 7, 7, 9]
target = 5
n = len(arr)
res = fun(arr,n,target)
print(res)
