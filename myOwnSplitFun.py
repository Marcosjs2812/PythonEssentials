# my own split() function starts here #############################################
def mysplit(strng):
    pasa = 0
    for x in strng:
        if x.isalpha():
            pasa = 1
    if strng == "" or pasa == 0:
        return ([])
    elif pasa == 1:
        lst = []
        fnd = strng.find(" ")
        while fnd != -1:
            lst.append(fnd)
            fnd = strng.find(" ",fnd+1)
        newString = []
        aux = 0
        for x in lst:
            if strng[aux:x] != "" and strng[aux:x] != " ":
                newString.append(strng[aux:x].strip())
                aux = x + 1
        try:
            if strng[lst[-1] + 1] != "" and strng[lst[-1] + 1] != " ":
                newString.append(strng[lst[-1]+1:])
        except (IndexError):
            pass
        return newString

# my own split() function ends here #############################################
