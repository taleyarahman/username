#GRADE FUNCTION
# name=input("enter name: ")

# m=int(input("enter maths marks: "))
# e=int(input("enter english marks: "))
# p=int(input("enter physics marks: "))


# def cal_avg(m,e,p):
#     avg= round((m + e+ p)/3 ,2)
#     return avg #forgot to write return avg !!


# def get_grade(avg):
#     if avg >=90:
#         return "A" #was calling "name " variable from outside the function
#     elif avg>=80:
#         return "B"
#     elif avg >=70: #used "if" instead of "elif"
#         return "C"
#     elif avg >=60:
#         return "D"
#     else:
#         return "F"

# avg = cal_avg(m, e, p)
# grade = get_grade(avg)
# print(name , "Scored" , avg ,"and got a", grade)

#fact(n)=n* fact(n-1)
#n!= n * (n-1)!

# def fact(n):
#     if n<0:
#         return None
#     if n==0:
#         return 1
#     return fact(n-1)*n

# print(fact(5))
# print(fact(-1))
# print(fact(0))

#Recursive digit sum
# n = int(input("enter the n value: ")) #345


# def digit_sum(n):
#     if n ==0:
#         return n 
#     return n%10 + digit_sum(n//10)

# print(digit_sum(n))

#List sum 
nums = [4,5,6]

def list_sum(nums):
    if len(nums)==0:
        return 0
    return nums[0]  + list_sum(nums[1:])

print(list_sum(nums))
