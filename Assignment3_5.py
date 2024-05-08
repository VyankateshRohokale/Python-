import Assignment3_module

def main():
    print("How many elements do you want to enter : ")
    no = int(input())
    print("Enter elements : ")

    arr = list()

    for cnt in range(0,no):
        arr.append(int(input()))

    

    print("Entered array is : ",arr)

  

    ans = list()
    ans = Assignment3_module.ListPrimeChk(arr)

    sum = 0

    sum = Assignment3_module.ListPrimeSum(ans)
    print("Addition of prime numbers is : ",sum)

if __name__ == "__main__":
    main()

