import Assignment3_module

def main():
    print("How many elements do you want to enter : ")
    no = int(input())
    print("Enter elements : ")

    arr = list()

    for cnt in range(0,no):
        arr.append(int(input()))

    

    print("Entered array is : ",arr)

  

    ans = 0
    ans = Assignment3_module.ListFeq(arr)

    print("frequency of targeted number is : ",ans)


if __name__ == "__main__":
    main()

