import sys

def main():
    print("Addition of arguments is : ")

    ans = 0
    ans = int(sys.argv[1]) +  int(sys.argv[2])

    print(ans)


if __name__ == "__main__":
    main()

