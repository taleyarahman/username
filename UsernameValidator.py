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

name = input("enter student name : ")
maths = int(input("maths marks: "))
english = int(input ("english marks"))
phy = int(input("physics marks"))
avg= float((maths + english + phy)/3)
if avg >= 90:
    print(name, "scored" , avg , "and got a A")
elif avg >=80 :
    print(name, "scored" , avg , "and got a B")
elif avg >=70:
    print(name, "scored" , avg , "and got a C")
elif avg >=60:
    print(name, "scored" , avg , "and got a D")
else:
    print(name, "scored" , avg , "and got a F")
