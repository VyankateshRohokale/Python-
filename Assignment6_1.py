import threading


def displayodd(no):

    print("ODD Thread is running ...")
    
    no = no * 2
    no = no + 1

    for i in range(no):
        if(i % 2 == 1):
            print(i,end="  ")

    print("")



def displayeven(no):
    print("EVEN Thread is running ...")
    no = no * 2
    no = no + 1
    
    for i in range(1,no):
        if(i % 2 == 0):
            print(i,end = "  ")

def main():

    no = int(input("How many number of even and odd numbers you want to display : "))
    
    even = threading.Thread(target = displayeven,args = (no,))
    odd = threading.Thread(target = displayodd,args = (no,))

    even.start()
    odd.start()

    even.join()
    odd.join()

    print("Exit from main...")



if __name__ == "__main__":
    main()