import os
import multiprocessing

def task1(no):
    print("Executing first task")
    print("PID of task1 : ",os.getpid())
    print("PPID of task1 : ",os.getppid())

def task2(no):
    print("Executing first task")
    print("PID of task2 : ",os.getpid())
    print("PPID of task2 : ",os.getppid())  

def main():
    print("PID of running process : ",os.getpid())
    print("PID of parent process is command prompt is : ",os.getppid())

    value = 11
    p1 = multiprocessing.Process(target = task1,args = (value,))
    p2 = multiprocessing.Process(target = task2,args = (value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
