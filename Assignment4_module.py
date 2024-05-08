
power = lambda num : num**2

mul = lambda num1,num2 : num1*num2


def filterOfQ3(arr = list()):
    no = 69
    filterarr = list()

    for i in range(len(arr)):
        if(arr[i] > no ):
            filterarr.append(arr[i])

    print("Filtered array is : ",filterarr)

    mapOfQ3(filterarr)


def mapOfQ3(arr = list()):
    
    for i in range(0,len(arr)):
        arr[i] = arr[i] + 10

    print("List after map is : ",arr)
    reduceOfQ3(arr)


def reduceOfQ3(arr = list()):
    sum = 0

    for i in range(0,len(arr)):
        sum = arr[i] + sum

    print("Output is : ",sum)
   
    

def filterOfQ4(arr = list()):
    
    filterarr = list()

    for i in range(len(arr)):
        if(arr[i] % 2 == 0):
            filterarr.append(arr[i])

    print("Filtered array is : ",filterarr)

    mapOfQ4(filterarr)


def mapOfQ4(arr = list()):
    
    for i in range(0,len(arr)):
        arr[i] = arr[i] ** 2

    print("List after map is : ",arr)

    reduceOfQ4(arr)
    

def reduceOfQ4(arr = list()):
    sum = 0

    for i in range(0,len(arr)):
        sum = arr[i] + sum

    print("Output is : ",sum)
    

def filterOfQ5(arr=list()):
    filterarr = list()
    print("In filter")
    for i in range(0, len(arr)):
        k = 0
        for cnt in range(2, arr[i]):
            if arr[i] % cnt == 0:
                k = 1
                break
        if k == 0:
            filterarr.append(arr[i])

    print("list after filter : ",filterarr)

    mapOfQ5(filterarr)

def mapOfQ5(arr= list()):

    for i in range(0,len(arr)):
        arr[i] = arr[i] * 2

    print("List after map : ",arr)
    reduceOfQ5(arr)
    
def reduceOfQ5(arr= list()):
    max = 0
    
    for i in range(0,len(arr)):
        if(max < arr[i]):
            max = arr[i]

    print("Reduce is : ",max)
