import threading


def fun1(no1):

    for i in range(1,no1+1):
        print(i,end=" ") 


def fun2(no2):

    for i in range(50,no2,-1):
        print(i,end=" ")

def main():

    print("Thread one : ")

    no1 = 50
    no2 = 0

    thread1 = threading.Thread(target = fun1,args = (no1,))
    thread2 = threading.Thread(target = fun2,args = (no2,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()



if __name__ == "__main__":
    main()