# Complete the freqQuery function below.
def freqQuery(queries):
    my_dict = {}
    out = []
    for x,y in queries:
        # print(f"x= {x}, y ={y}")
        if x == 1:
            val = my_dict.get(y)
            if val:
                my_dict[y]= val+1
            else:
                my_dict[y]= 1
        if x==2:
            val = my_dict.get(y)
            if val:
                my_dict[y]= val-1
     
        if x==3:
            if y in my_dict.values():
                print("1")
                out.append(1)
            else:
                print("0")
                out.append(0)
    return out



# queries = [[1, 5],
# [1, 6],
# [3, 2],
# [1 ,10],
# [1 ,10],
# [1 ,6],
# [2 ,5],
# [3, 2]]
queries = [ [1,1],
           [2,2],
           [3,2],
           [1,1],
           [1,1],
           [2,1],
           [3,2]]

freqQuery(queries)