# #shopping cart tracker
# cart = ["chips","lemon","apples" ,"mango","cake"]
# lencart = len(cart)
# print(lencart)
# cart.append("mango shake")
# cart.remove("lemon")
# print(cart)
# print(cart[2])
# cart_tuple =tuple(cart)
# print(cart_tuple)
# cart_tuple[3] = "me" #error because tuples are immutable.

#Inventory Reconciliation   

# day1 = ["pen", "notebook", "stapler", "eraser", "tape"]
# day1_counts = (120, 45, 30, 200, 75)

# day2 = ["notebook", "tape", "pen", "eraser", "stapler"]
# day2_counts = (40, 70, 115, 195, 28)

# worst_item= None
# worst_drop = None

# for i , item in enumerate(day1):

#     if item in day2:

#         index = day2.index(item)
#         diff = day1_counts[i] - day2_counts[index]
#         print(item ,diff)


#     if  worst_drop is None or  diff < worst_drop:
#         worst_drop = diff
#         worst_item = item

# print("biggest drop in sales is for item:" , worst_item , "with a drop of " , worst_drop)

#Grade Book Merge
midterm = [("Ravi", 72), ("Sneha", 88), ("Arjun", 65), ("Divya", 91)]
final = [("Divya", 85), ("Arjun", 70), ("Ravi", 80), ("Sneha", 92)]

results=[] 

for student in midterm:
    name = student[0]
    midterm_score = student[1]

    for s2 in final:

        if s2[0] == name:
            final_score = s2[1]
            total = round((midterm_score * 0.4) + (final_score * 0.6), 2)
            results.append((name, total))

for r in results:
        print(r[0], ":", r[1])

best_student = None
best_score = None

for r in results:
    if best_score is None or r[1] > best_score:
        best_score = r[1]
        best_student = r[0]

print("Best student is:", best_student, "with a score of:", best_score)

try:
     results[0][1]=100
except TypeError as e:
     print("Error:" , e)
     

