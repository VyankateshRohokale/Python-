import Assignment4_module


def main():
    no = 0
    no = int(input("How many elements are you going to enter in the list? : "))
    arr = list()

    print("Enter the elements of the list :")
    for cnt in range(0,no):
        arr.append(int(input()))

    

    print("Entered array is : ",arr)

    ans = 0
    ans = Assignment4_module.filterOfQ3(arr)




if __name__ == "__main__":
    main()