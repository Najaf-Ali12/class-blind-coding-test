#function lectures
#REAL LIFE EXERCISES
#1:MOVIE TICKET PRICES
#using functions make a programme that calculates movie ticket price based on age(adult,child,senior)and
#day of the week(weekend,weekday)
#modify the function to offer discounts for group and family packages.
def weekend_ticket(x):
    if day=="weekend":
        if age=="child":
            return 290
        if age=="adult":
            return 550
        if age=="senior":
            return 450
age=input("tell whether you are adult/child/senior")
day=input("tell whether the day is weekend or weekday")
group=input("are you in group or with family,yes or no")
y=weekend_ticket(age)
if day=="weekend":
    print("the ticket price for you is",y,"PKR")
def weekday_ticket(y):
    if day=="weekday":
        if age=="child":
            return 200
        if age=="adult":
            return 400
        if age=="senior":
            return 300
t=weekday_ticket(age)
if day=="weekday":
    print("the ticket price for you is ",t,"PKR")
if group=="yes":
    if day=="weekend":
        print("the discounted ticket price for each person in group is",y,"-50")
    if day=="weekday":
        print("the discounted ticket price for each person in group is",t,"-30")



