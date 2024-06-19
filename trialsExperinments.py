"""cart = [10,20,30,40,50]
for item in cart:
    if item >=50:
        print("P")
        break
    print (item)
else:
    print("S")"""

cart = [10, 20, 30, 40, 50]
i = 0
while i < len(cart):
  item = cart[i]
  if item >= 50:
    print("P")
    break
  print(item)
  i += 1
else:
  print("S")