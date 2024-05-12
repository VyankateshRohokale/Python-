
def CheckEven(no):
    if(no% 2 == 0):
        print("It is even number..")
    else:
        print("It is odd number..")

def main():
    a = int(input("Enter a number : "))

    CheckEven(a)


main()    