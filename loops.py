def displaywhile(no1):
    no = 0
    while(no < 5):
        print("marvellous")

def displayfor(no1):

    for i in range(no1):
        print("Marvellous")

def main():

    print("How many times you want to iterate : ")
    no = 0
    no = int(input())

    displayfor(no)
    displaywhile(no)


if __name__ == "__main__":
    main()