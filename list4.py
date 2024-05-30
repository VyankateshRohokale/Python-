

def main():
    print("Enter number of elements you want to enter : ")

    
    arr = list()
    arrlen = int(input())
    print("enter elements : ")

    for i in range(arrlen):
        no = int(input())
        arr.append(no)

    print(arr)
if __name__ == "__main__":
    main()

    