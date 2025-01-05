def lowerbound (arr,target , n):
    high = n -1 
    low = 0 
    ans = n 
    while ( low <= high ):
        mid = ( low + high )//2 
        if ( arr[mid ]>= target ):
            ans = mid 
            high = mid -1 
        else :
            low = mid + 1
    return ans 
def upperbound(arr,target,n):
    high = n -1 
    low = 0 
    ans = n 
    while(low <= high):
        mid = (low+high)//2 
        if(arr[mid]>target):
            high = mid -1 
            ans = mid 
        else : 
            low = mid +1 
    return ans 
def findrange(arr,target,n):
    lb = lowerbound(arr,target,n)
    if lb == target or arr[lb] != target :
        return -1 , -1 
    ub = upperbound(arr,target,n)-1 
    return lb , ub
arr = [ 1,3,5,5,5,7,7,8,9]
target = 7
n = len(arr)
print(findrange(arr,target,n))