def maxMin(k, arr):
    # Write your code here
    arr.sort()
    min = set() # float('inf')
    
    for i in range(len(arr)-k+1):
        min.add(arr[i+k-1]-arr[i]) 
    return sorted(list(min))[0]

arr = [1,4,7,2]
k = 2
out = maxMin(k, arr)
print(out)