import threading

def faceven(no):

    sumeven = 0

    for i in range(no + 1):
        if(i % 2 == 0):
            sumeven = sumeven + i

    print("Sum of all even number is : ",sumeven)

def facodd(no):

    sumodd = 0

    for i in range(no + 1):
        if(i % 2 == 1):
            sumodd = sumodd + i

    print("Sum of all odd number is : ",sumodd)




def main():

    no = int(input("Enter a number : "))

    even = threading.Thread(target = faceven,args = (no,))

    odd = threading.Thread(target = facodd,args = (no,))

    even.start()
    odd.start()

    even.join()
    odd.join()

    print("Exit from main..")




if __name__ == "__main__":
    main()