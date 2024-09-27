import sys


def minimumAbsoluteDifference(arr):
    # Write your code here
    # abs_diff = sys.maxsize
    abs_diff = float('inf')
    print(abs_diff)
    arr.sort()
    print(arr)
    for i in range(len(arr)-1):
        # print(f"abs(arr[i]-arr[j])=  {abs(arr[i]-arr[j])}  arr[i] = {arr[i]}, arr[j] = {arr[j]}")
        if abs(arr[i]-arr[i+1])< abs_diff:
            abs_diff = abs(arr[i]-arr[i+1])
    return abs_diff

arr = [-2,2,4]
out = minimumAbsoluteDifference(arr)
print(out)