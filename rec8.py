i = 1
fact = 1

def displayR(no1):
    global i
    global fact
    if(no1 >= i):
        fact = fact * no1
        no1 = no1 - 1
        factorial(no1)
        
    return fact

def main():
    no = int(input("Enter the number : "))
    displayR(no)

if __name__ == "__main__":
    main()

d