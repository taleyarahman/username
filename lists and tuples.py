#shopping cart tracker
cart = ["chips","lemon","apples" ,"mango","cake"]
lencart = len(cart)
print(lencart)
cart.append("mango shake")
cart.remove("lemon")
print(cart)
print(cart[2])
cart_tuple =tuple(cart)
print(cart_tuple)
cart_tuple[3] = "me"