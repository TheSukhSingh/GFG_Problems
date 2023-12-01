def square(s):

    for i in range(s):
        if i == 0:
            
            print("* "*s)
            
        elif i > 0 and i < s-1:
            
            print("*", " "*(s-1), "*")
            
        else:
            print("* "*s)