# 10.	Profit or Loss: Compare cost price and selling price to determine profit/loss.
CostPrice = int(input("Enter the Cost Price: "))
SellingPrice = int(input("Enter the Selling Price: "))
if SellingPrice > CostPrice:
    print("You are in profit: ₹",SellingPrice - CostPrice)
elif SellingPrice == CostPrice:
    print("No profit and no Loss")
else:
    print("OOps you are in loss: ₹",CostPrice - SellingPrice)





