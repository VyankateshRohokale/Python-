import sys

def addition(no1,no2):
    ans = 0
    ans = no1 + no2
    return ans


def main():
    print("welcome to the application : "+sys.argv[0])

    if(len(sys.argv) != 3 ):
        print("Invalid number of arguments..")
        print("Please provide 2 numbers in arguments to perform addition")
        return 

    if(len(sys.argv) >= 3 ):
        result = addition(int(sys.argv[1]), int(sys.argv[2]))

    result = addition(int(sys.argv[1]), int(sys.argv[2]))

    print("Addition is : ",result)

if __name__ == "__main__":
    main()