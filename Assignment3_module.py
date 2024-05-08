def ListSum(arr2 = list()):
    sum = 0
    for i in range(0,len(arr2)):
        sum = sum + arr2[i]

    return sum



def ListMax(arr2 = list()):
    max = 0
    for i in range(0,len(arr2)):
        if(max < arr2[i]):
            max = arr2[i]

        
    return max


def ListMin(arr2 = list()):

    min = arr2[0]
    for i in range(0,len(arr2)):
        if(min > arr2[i]):
            min = arr2[i]


    return min


def ListFeq(arr2 = list()):

    feq = 0
    target = int(input("What is the targeted number : "))
    for i in range(0,len(arr2)):
        if(arr2[i] == target):
            feq = feq + 1

    
    return feq

def ListPrimeChk(arr2 = list()):

    prime = list()

    for num in arr2:
        is_prime = True
        if num <= 1:
            is_prime = False
        else:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
        if is_prime:
            prime.append(num)

    print(prime)

    return prime
            

def ListPrimeSum(arr2 = list()):
  
    add = 0
    for i in range(0,len(arr2)):
        add = add + arr2[i]

    return add