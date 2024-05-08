import Assignment4_module


def main():
    no = 0
    no = int(input("Enter a Number : "))

    ans = 0
    ans = Assignment4_module.power(no)

    print("ans is : ",ans)


if __name__ == "__main__":
    main()