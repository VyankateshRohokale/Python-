import os 

def cube(no):
    print("PID is : ",os.getpid())
    return no*no*no


def main():
    arr = [10,20,30,40]
    result = []

    for value in arr:
        result.append(cube(value))

    print(result)


if __name__ == "__main__":

    main()
