def cipher(s):
    res=""
    for i in s:
        if 97<=ord(i)<=122:
            res+=chr(219-ord(i))
        else:
            res+=i
    return res
s="abcdefghijklmnopqrstuvwxyz"
print(cipher(s))