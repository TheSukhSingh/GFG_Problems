def alphabets(c1, c2):
    a = ord(c1)
    
    while a <= ord(c2):
        print(chr(a), end=" ")
        a += 1