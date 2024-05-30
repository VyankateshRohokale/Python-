i = 1

def displayR(no1):
    global i
    if(i <= no1):
        print(i)
        i = i + 1
        displayR(no1)
       

def main():
    
    displayR(no)

if __name__ == "__main__":
    main()

