def fun (arr,target,n):
    low = 0 
    high = n -1 
    while(low <= high):
        mid = (low+high)//2
        if (mid * mid * mid == target ):
            return mid 
        elif (mid*mid*mid > target ):
            high = mid - 1 
        else : 
            low = mid +1 
    return 0 
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
target = 27 
n = len(arr)
print(fun(arr,target,n))