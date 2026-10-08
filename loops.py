#checking lays Ingredients 
# lays=("Potato","Edible vegetable oil ","Salt." ,"Sugar","Maltodexterin")
# for spices in lays:
#     if(spices == "Maltodexterin","caramel colour III ans IV", "TBHQ","Diacetyl","Modified food starch"):
#         print("dont eat")
#         break
#     print(spices)
# else:
#     print("eat")

# for i in range(5,51,5):
#     print(i)

# n = 5
# for i in range(1,11):
#     print(n*i)

# n = int(input("enter a number : "))
# sum = 0
# i =1
# while i<=n:
#     sum+=i
#     i+=1

# print("total sum is : ", sum)

n = int(input("enter the number: "))
fact=1
i=1
while i <=n:
    fact*=i
    i+=1

print("factorial of ",n , "is" ,fact)

n = int(input("enter the number: "))
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial = ", fact)