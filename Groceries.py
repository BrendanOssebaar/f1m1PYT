shoppinglist=["Apple", "Pear", "Melon"]
Grocerielist=["Apple", "Pear", "Melon"]
a=0
for x in shoppinglist:
    for y in Grocerielist:
        if x == y:
            a+=1
if a== len(shoppinglist):
    print("Done shopping")
else:
    print("continue shopping")