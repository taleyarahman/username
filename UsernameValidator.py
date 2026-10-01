name = input("enter name: ")
age = int(input("enter age: "))
slicedname = name[:3]
short = slicedname.lower()
username =short + (str(age))
print("your username is :", username)
if age < 13:
    print("Too young for this platform")
elif age <= 17:
    print("Teen account created :",username)
else:
    print("Adult account created:",username)