def restaurant(x):
    return x
items=int(input("enter the number of items"))
quantity=int(input("enter the total quantity of items in kilo"))
price=int(input("enter the  average price of each item"))
friends=int(input("enter the number of friends who have to pay"))
discount=int(input("enter the discount amount"))
total_bill=items*quantity*price
total_amount=restaurant(total_bill)
tax=total_amount*int(input("enter TAX PERCENTAGE"))/100
print("CUSTOMERS' total bill is ",total_amount,"PKR")
def restauranta(y):
    return y
billa=(total_amount+tax)-discount
modified_bill=restauranta(billa)
print("and the bill(with tax and discount) CUSTOMERS have to pay is",modified_bill,"PKR")
print("the bill each one has to pay is",modified_bill/friends,"PKR")

