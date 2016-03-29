numberOfItems = int(input("Enter number of items: "))
while numberOfItems < 0:
    print("Invalid number of items!")
    numberOfItems = int(input("Enter number of items: "))

shippingCostPerItem = int(input("Enter shipping cost per item: "))
totalShippingCost= numberOfItems * shippingCostPerItem

if totalShippingCost>100:
    finalCost = totalShippingCost - (totalShippingCost * 0.1)
else:
    finalCost = totalShippingCost
print("$",finalCost,sep='')


