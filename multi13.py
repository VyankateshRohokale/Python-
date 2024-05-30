import multiprocessing
import os
import time

def cube(no):
    print("PID is : ",os.getpid())
    return no*no*no


def main():
    starttime = time.time()
    arr = [100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000,1100000,1200000,1300000,1400000]
    result = []
    
    for value in arr:
        result.append(cube(value))


    print(result)
    endtime = time.time()
    print("time required for execution was : ",endtime-starttime)


if __name__ == "__main__":

    main()


    