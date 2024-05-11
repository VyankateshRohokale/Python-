i = 1
digit = 0
sum = 0
fac = 1

def pattern1(no):
    global i 

    print("*",end="  ")
    
    if(i < no):
        i = i + 1
        pattern1(no)

def pattern2(no):
    global i 

    print(i,end="  ")
    
    if(i < no):
        i = i + 1
        pattern2(no)

def pattern3(no):

    global i 

    print(no,end="  ")

    if(no > i):
        no = no - 1
        pattern3(no)

def pattern4(no):
    global digit
    global sum

    digit = no % 10
     
    sum = sum + digit

    no = no / 10
   
    if(no > 0):
        pattern4(no)

    return sum

def pattern5(no):
    global fac
    global i 

    fac = fac * i 
    i = i + 1
    if(no >= i):
        pattern5(no)

    return fac
    
    

    