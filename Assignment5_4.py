import Assignment5_module

def main():

    no = int(input("Enter a Number : "))
    ans = 0
    ans = Assignment5_module.pattern4(no)

    print("sum of digits is : ", ans)



if __name__ == "__main__":
    main()