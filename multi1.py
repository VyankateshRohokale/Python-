import os

def main():
    print("PID of running process : ",os.getpid())
    print("PID of parent process is command prompt is : ",os.getppid())

if __name__ == "__main__":
    main()
    