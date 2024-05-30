def add(*no):
   
    ans = 0
    print(type(no))
    print(len(no))
    
    for i in no:
        ans = ans + i

    return ans

    


result = add(10,20,30,40,50)
print(result)