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

day1 = ["pen", "notebook", "stapler", "eraser", "tape"]
day1_counts = (120, 45, 30, 200, 75)

day2 = ["notebook", "tape", "pen", "eraser", "stapler"]
day2_counts = (40, 70, 115, 195, 28)

worst_item= None
worst_drop = None

for i , item in enumerate(day1):

    if item in day2:

        index = day2.index(item)
        diff = day1_counts[i] - day2_counts[index]
        print(item ,diff)


    if  worst_drop is None or  diff < worst_drop:
        worst_drop = diff
        worst_item = item

print("biggest drop in sales is for item:" , worst_item , "with a drop of " , worst_drop)
