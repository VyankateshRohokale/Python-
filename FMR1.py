
def CheckEven(no):
    return (no % 2 == 0)

def Increase(no):
    return no + 1

def add(a,b):
    return a+b

def main():
    data = [11,14,20,23,18,16,15,20]

    print("Data from input list : ",data)

    Fdata = list(filter(CheckEven,data))
    print("data after filter activity : ",Fdata)

    Mdata = list(map(increase, Fdata))
    print("data after map activity : ",Mdata)

    Rdata = reduce(add, Mdata)
    print("data after reduce activity is : ",Rdata)


if __name__ == "__main__":
    main()