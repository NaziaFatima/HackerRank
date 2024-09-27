############# WORK IN PROGRESS #############

def caesarCipher(s, k):
    arr = list(s)
    for i in range(len(s)):
        # ASCII alphabet characters are the letters 'A' through 'Z' and 'a' through 'z', which are assigned numbers 65 through 90 and 97 through 122 in the ASCII character encoding standard
        if (ord(s[i]) >= 65 and  ord(s[i]) <=90): # Capitals
            new_ord = ord(s[i])+k
            if new_ord> 90:
                diff = new_ord-90
                rotated_ord = 64+diff
                # print("rotated_order = ", rotated_ord)
                # print("chr(rotated_ord)= ", chr(rotated_ord))
                arr[i]= chr(rotated_ord)
            else:
                arr[i]= chr(new_ord)
        elif (ord(s[i])>= 97 and  ord(s[i])<= 122): #Small letters
            new_ord = ord(s[i])+k
            # print("new_ord", new_ord)
            if new_ord>122:
                diff = new_ord-122
                rotated_ord = 96+diff
                arr[i] = chr(rotated_ord)
            else:
                arr[i]= chr(new_ord)
        else:
            arr[i]=s[i]
    # print(arr)
    return ("".join(arr))

s = "Always-Look-on-the-Bright-Side-of-Life"
k = 5

caesarCipher(s, k)