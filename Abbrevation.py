def abbreviation(a, b):
    # Write your code here 
    my_dict = {}
    for i in a:
        my_dict[i] = my_dict[i]+ 1 if my_dict.get(i) else 1 # fill the dict with char counts
    for i in b:
        if i.upper() in my_dict.keys().upper():
            print("my_dict.keys()", my_dict.keys())
            pass
        else:
            return "No" 
        # if my_dict.get(i) :
        #     my_dict[i] +=1 
        # else:
        #     my_dict[i]=1
    print(my_dict)

a = "AbcDDE"
b = "ABDE"
out = abbreviation(a, b)
print(out)