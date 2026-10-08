#checking lays Ingredients 
# lays=("Potato","Edible vegetable oil ","Salt." ,"Sugar","Maltodexterin")
# for spices in lays:
#     if(spices == "Maltodexterin","caramel colour III ans IV", "TBHQ","Diacetyl","Modified food starch"):
#         print("dont eat")
#         break
#     print(spices)
# else:
#     print("eat")


#PASSWORD RETRY 
# real_pass= "python123"

#WHILE LOOP
# count =0
# granted=False #switch is OFF

# while count<=2:
#     password=input("enter the password : ")
#     count+=1

#     if real_pass==password:
#         print("Access granted")
#         granted=True  #switch in ON
#         break
#     else:
#         print(3-count ,"Attempts left")

# if granted==False:
#     print("Account locked. ")

# #FOR LOOP
# for i in range(3):
#     password=input("enter the password: ")
#     if real_pass==password:
#         print("access granted")
#         break
#     else:
#         print(2-i,"attempts left")
# else:
#     print("Account locked")

#Digit Sum
num = int(input("enter a positive integer: "))  #4896
total = 0
count = 0

while num > 0:
    digit= num // 10 #489
    total += num % 10 #6
    count+=1
    num = digit

print("Sum of digits:", total)
print("Digit count: ", count)

