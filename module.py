def pattern(no1):
    
    for cnt in range(no1):
        for i in range(no1):
            print("*",end=" ")

        print(" ")

    
def facadd(no1):
    sum = 0
  
    for cnt in range(1,no1):
        if(no1 % cnt == 0):
            sum = sum + cnt
        
    return sum

def primenum(no1):
    k = 0
    for cnt in range(2,no1):
        if(no1 % cnt == 0):
            k = 1
            break

    return k



def pattern2(no1):

    no2 = no1
    
    for cnt in range(no2):
        for i in range(no1):
            print("*",end=" ")

        print(" ")
        no1 = no1 - 1

def pattern3(no1):
    no2 = 1
    
    for cnt in range(no1):
        for i in range(no1):
            print(no2,end=" ")
            no2 = no2 + 1

        print(" ")
        no2 = 1


def pattern4(no1):
    no2 = 1
    
    for cnt in range(no1):
        for i in range(cnt + 1):
            print(no2,end=" ")
            no2 = no2 + 1

        print(" ")
        no2 = 1


def numlen(no1):
    length = 0

    while no1 > 0:
        length = length + 1
        no1 = no1 // 10 

    return length

def numadd(no1):
    length = 0
    digit = 0
    sum = 0

    while no1 > 0:
        digit = no1 % 10
        sum = sum + digit
        no1 = no1 // 10 

    return sum

        