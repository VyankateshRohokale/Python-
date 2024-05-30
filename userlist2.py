def addition(data):
    sum = 0

    for no in data:
        sum = sum + no

    return sum

def main():
    print("Enter number of elements you want to enter : ")

    
    arr = list()
    arrlen = int(input())
    print("enter elements : ")

    for i in range(arrlen):
        no = int(input())
        arr.append(no)

    print("entered elements are : ",arr)

    result = addition(arr)
    print("Sumation of all elements : ",result)

if __name__ == "__main__":
    main()

    