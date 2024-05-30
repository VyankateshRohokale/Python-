i = 1

def displayR():
    global i
    if(i <= 5):
        print(i)
        i = i + 1
        displayR()
       

def main():
    
    displayR()

if __name__ == "__main__":
    main()

