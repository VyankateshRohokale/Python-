def add(no1,no2):

    print("Inside addition function")
    ans = 0
    ans = no1+no2
    return ans

def main():
    print("Inside main function")
    print("Enter 2 numbers :")

    a = int(input())

    b = int(input())

    result = add(a,b)

    print("addition is :" ,result)


main()

print("End of application..")
