

add = lambda a,b : a + b

increase = lambda no : no + 1

CheckEven = lambda no : no % 2 == 0

def filterX(task,Elements):
    result = []
    for no in Elements:
        ret = task(no)
        if(ret == True):
            result.append(no)

    return result

def mapX(task,Elements):
    result = []

    for no in Elements:
        ret = task(no)
        result.append(ret)

    return result  
    
def reduceX(task,Elements):
    sum = 0
   
    for no in Elements:
        sum = task(sum,no)

    return sum

    
