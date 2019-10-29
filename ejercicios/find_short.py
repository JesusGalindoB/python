def find_short(s):
    num = 0 
    L = len(s)
    s = s + " "
    for index, value in enumerate(s):
        if value == " ":
            sub_string = s[num:index]
            num = index + 1
            length = len(sub_string)
            if length <= L:
                L = length 
    return L # l: shortest word length


result = find_short("ProofOfStake Dogecoin")
print(result)


             