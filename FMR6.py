from functools import reduce

add = lambda a,b : a + b

increase = lambda no : no + 1

CheckEven = lambda no : no % 2 == 0

def filterX(task,Elements):
    result = []
    for no in Elements:
        ret = task(no)
        if(ret == True):
            result.append(no)

    return result



    


def main():
    data = [11,14,20,23,18,16,15,20]

    print("Data from input list : ",data)

    Fdata = list(filterX(CheckEven,data))
    print("data after filter activity : ",Fdata)

    Mdata = list(map(increase, Fdata))
    print("data after map activity : ",Mdata)

    Rdata = reduce(add, Mdata)
    print("data after reduce activity is : ",Rdata)


if __name__ == "__main__":
    main()