def Cal(no1,no2):
    def addition(x,y):
        return x+y

    def Substraction(x,y):
        return x-y

    ans1 = addition(no1,no2)
    ans2 = Substraction(no1,no2)
    return ans1,ans2

print("Enter two numbers : ")

a = int(input())
b = int(input())

result1,result2 = Cal(a,b)

print("Addition is :",result1 )
print("Sub is : ",result2)

