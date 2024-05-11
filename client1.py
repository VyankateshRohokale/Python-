from piyush import addition
from piyush import multiplication

def main():
    a = int(input("Enter 2 numbers : "))
    b = int(input())

    ans = 0
    ans = addition(a,b)

    print("addition is : ",ans)

    ans = 0
    ans = multiplication(a,b)

    print("multiplication is : ",ans)


main()

