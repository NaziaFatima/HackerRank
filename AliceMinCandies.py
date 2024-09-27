
def candies(n, arr):
    if n == 0:
        return 0
    out = [1] * n
    # Write your code here
    for i in range(n-1):
        if arr[i]< arr[i+1]:
            if not out[i]<out[i+1]:
                out[i+1]= out[i]+1
        # elif arr[i]>arr[i+1]:
        #     if out[i]>out[i+1]:
        #        pass
        #     else:
        #         count +=1
        #         out[i] = out[i+1]+1 
    for i in range(n-2, -1, -1):
        # print(f"i = {i} i+1 = {i+1} arr[i] = {arr[i]}  arr[i+1] = {arr[i+1]} out[i] = {out[i]} out[i+1] = {out[i+1]} ")
        if arr[i]> arr[i+1] and not out[i]> out[i+1]:
            # print(f"arr[i] {arr[i]}, arr[i+1] {arr[i+1]}, ")
            out[i+1] = out[i]+1
        # print(out)
    # print(sum(out))
    return sum(out)

arr = [4,6,4,5,6,2]
candies(6, arr)