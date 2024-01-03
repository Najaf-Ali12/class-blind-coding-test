#using functions make a programme that tells that either
#inputted number is even or odd
def checker(x):
    if x%2==0:
        return"even"
    if x%2==1:
        return"odd"
number=int(input("enter a number"))
result=checker(number)
print("your number is",result)
#make a programme using functions that tells the area of the rectangle 
def area(w,h):#w=width and H=height
    return w*h
width=int(input("please enter the width of rectangle in centimetres"))
height=int(input("please enter the height of rectangle in centimetres"))
result=area(width,height)
print("the area of the rectangle is",result,"centimetres")


