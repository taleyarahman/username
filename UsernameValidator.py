#create username 
# name = input("enter name: ")
# age = int(input("enter age: "))
# slicedname = name[:3]
# short = slicedname.lower()
# username =short + (str(age))
# print("your username is :", username)
# if age < 13:
#     print("Too young for this platform")
# elif age <= 17:
#     print("Teen account created :",username)
# else:
#     print("Adult account created:",username)

#enter the marks as input 
# name = input("enter student name : ")
# maths = int(input("maths marks: "))
# english = int(input ("english marks:"))
# phy = int(input("physics marks:"))
# avg= round((maths + english + phy)/3 , 2)
# if avg >= 90:
#     print(name, "scored" , avg , "and got a A")
# elif avg >=80 :
#     print(name, "scored" , avg , "and got a B")
# elif avg >=70:
#     print(name, "scored" , avg , "and got a C")
# elif avg >=60:
#     print(name, "scored" , avg , "and got a D")
# else:
#     print(name, "scored" , avg , "and got a F")

#username and password validator
username = input("enter username : ")
password = input("enter password : ")
len1 = len(password)
if len1 >= 8:
    print( password , "is valid")
else:
    print( password , "is invalid")
