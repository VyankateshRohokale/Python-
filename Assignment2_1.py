import arithmetic


def main():

    a = int(input("Enter 2 numbers : "))
    b = int(input())

    result = 0

    result = arithmentic.add(a,b)

    print("addition : ",result)

    result = arithmentic.sub(a,b)

    print("substraction : ",result)

    result = arithmentic.mul(a,b)
    print("multiplication : ",result)


    result = arithmentic.div(a,b)

    print("divition  : ",result)





main()