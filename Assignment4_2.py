import Assignment4_module


def main():
    no = 0
    no1 = int(input("Enter Two Numbers : "))
    no2 = int(input())
    ans = 0
    ans = Assignment4_module.mul(no1,no2)

    print("Multiplication is : ",ans)


if __name__ == "__main__":
    main()