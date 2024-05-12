from functools import reduce

add = lambda a,b : a + b

increase = lambda no : no + 1

CheckEven = lambda no : no % 2 == 0

def main():
    data = []
    no = 0
    no = int(input("Enter how many elements you want to enter : "))
    print("Enter elements : ")
    for i in range(0,no):
        data.append(int(input()))

    print("Data from input list : ",data)

    Fdata = list(filter(CheckEven,data))
    print("data after filter activity : ",Fdata)

    Mdata = list(map(increase, Fdata))
    print("data after map activity : ",Mdata)

    Rdata = reduce(add, Mdata)
    print("data after reduce activity is : ",Rdata)


if __name__ == "__main__":
    main()

