
def countTriplets(arr, r):
    n = len(arr)
    print(f"n =  {n}")
    out_list = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i]< arr[j]< arr[k]:
                    if arr[i]/r < arr[j]/r < arr[k]/r:
                        if i<j<k and arr[i]/arr[j]==r and arr[k]/arr[j]==r:
                            out_list.append([i,j,k])
                            # print(f"arr[i] = {arr[i]}, arr[j] = {arr[j]}, arr[k] = {arr[k]}")
                            # print(f"i = {i}, j = {j},k = {k}")
    
    return len(out_list)



arr=[1 ,3 ,9 ,9 ,27, 81]
r = 3
countTriplets(arr, r)