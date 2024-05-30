import multiprocessing
import os

def cube(no):
    print("PID is : ",os.getpid())
    return no*no*no


def main():
    arr = [10,20,30,40]
    result = []
    
    p = multiprocessing.Pool()
    result = p.map(cube,arr)
    p.close()
    p.join()


    print(result)


if __name__ == "__main__":

    main()


    