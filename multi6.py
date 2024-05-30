import threading
import os


def displayodd(no):
    print("PID of odd process ",os.getpid())
    print("TID of odd thread ",threading.get_ident())
    no = no * 2
    no = no + 1

    for i in range(no):
        if(i % 2 == 1):
            print(i,end="  ")

    print("")



def displayeven(no):
    print("PID of even process ",os.getpid())
    
    print("TID of even thread ",threading.get_ident())
    no = no * 2
    no = no + 1
    
    for i in range(1,no):
        if(i % 2 == 0):
            print(i,end = "  ")

def main():

    no = int(input("How many number of even and odd numbers you want to display : "))
    
    print("PID of main process ",os.getpid())
    p1 = threading.Thread(target = displayeven,args = (no,))
    p2 = threading.Thread(target = displayodd,args = (no,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main process")
    



if __name__ == "__main__":
    main()