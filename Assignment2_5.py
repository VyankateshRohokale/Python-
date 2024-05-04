import module

def main():
    no = int(input("Enter a Number : "))

    ans = module.primenum(no)

    if(ans == 1):
        print("It is not Prime Number..")

    else:
        print("It is a Prime Number..")


if __name__ == "__main__":
    main()