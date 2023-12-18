#MAKE A RESTAURANT BILL CALCULATOR
#Write a programme that asks the user following information for their restaurant bill
#number of people
#cost of each meal
#sales tax percentage
#TIP percentage
#BASED ON THE INFORMATION PROVIDED CALCUTE AND PRINT THE FOLLOWING
#Total cost of food
#Total sales tax
#total tip amount
#total bill amount per person
people=int(input("please enter the number of persons involved in meal"))
meal=int(input("enter the cost of meals"))
biryani=int(input("enter the cost of biryani"))
salan=int(input("enter the cost of salan"))
salestaxPercentage=int(input("enter the ST percentage"))
TIP=int(input("enter the tip percentage"))
totalcost=int(meal+biryani+salan)
print("total cost of your food is:",totalcost)
salestax=(totalcost*salestaxPercentage)/100
print("sales tax that you have to pay is: ",salestax)
tipamount=(TIP*totalcost)/100
print("the tip that you will pay is:",TIP*totalcost/100)
totalbill=totalcost+salestax+tipamount
print("total bill that you will pay is :",totalcost+salestax+tipamount)
individuabill=print("individually each person has to pay",totalbill/people,"in bill")





        
