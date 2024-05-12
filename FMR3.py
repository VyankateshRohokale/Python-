from functools import reduce

 

def main():
    data = [11,14,20,23,18,16,15,20]

    print("Data from input list : ",data)

    Fdata = list(filter((lambda no : no % 2 == 0),data))
    print("data after filter activity : ",Fdata)

    Mdata = list(map((lambda no : no + 1), Fdata))
    print("data after map activity : ",Mdata)

    Rdata = reduce((lambda a,b : a + b), Mdata)
    print("data after reduce activity is : ",Rdata)


if __name__ == "__main__":
    main()