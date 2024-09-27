def countingSort(arr):
    # Write your code here
    out = [0 for i in range(100)]
    print(out )
    for i in range(len(arr)):
        out[arr[i]] += 1
    return out 

arr= [1,1,3,2,1]
countingSort(arr)
