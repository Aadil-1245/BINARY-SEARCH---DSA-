# COUNT THE NUMBER OF OCCURANCES IN THE SORTED ARRAY - BINARY SEARCH 
def firstocc(arr,target,n):
    high = n -1 
    low = 0 
    first = -1 
    while(low <= high):
        mid = (low+high)//2 
        if(arr[mid] == target):
            first = mid 
            high = mid -1  
        elif (arr[mid]< target):
            low = mid +1 
        else:
            high = mid -1 
    return first 
def lastocc(arr,target,n):
    high = n -1 
    low = 0 
    last = -1 
    while(low <= high):
        mid = (low+high)//2 
        if (arr[mid]==target):
            last = mid 
            low = mid +1 
        elif(arr[mid] < target):
            high = mid -1 
        else :
            low = mid + 1
    return last
arr = [ 1,2,3,3,3,3,3,6,7,8]
target = 6
n = len(arr)
print(firstocc(arr,target,n),lastocc(arr,target, n ))