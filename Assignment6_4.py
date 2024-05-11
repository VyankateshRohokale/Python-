import threading
import os

def smallfun(string):
    print("PID of SMALLFUN is : ",os.getpid())
    count = 0
    for char in string:
        if char.islower():
            count += 1
    print("Total lowercase characters: ", count)

def capitalfun(string):
    print("PID of CAPITALFUN is : ",os.getpid())
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    print("Total uppercase characters: ", count)

def digitfun(string):
    print("PID of DIGITFUN is : ",os.getpid())
    count = 0
    for char in string:
        if char.isdigit():
            count += 1
    print("Total digits: ", count)

def main():
    string = input("Enter a string: ")

    small = threading.Thread(target=smallfun, args=(string,))
    capital = threading.Thread(target=capitalfun, args=(string,))
    digit = threading.Thread(target=digitfun, args=(string,))

    small.start()
    capital.start()
    digit.start()

    small.join()
    capital.join()
    digit.join()

    print("Exit from main function....")

if __name__ == "__main__":
    main()