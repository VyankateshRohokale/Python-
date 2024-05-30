
evenodd = lambda a : (a%2==0) 


def main():
    no = int(input("Enter the number  : "))
    ret = evenodd(no)
    if(ret == 0):
        print("odd")
    else:
        print("even")
if __name__ == "__main__":
    main()
    