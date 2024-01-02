#write a programme that asks for a persons age,employment status, marital status and then determines the insurance plan
#according to table given by sir:
age=int(input("enter your age"))
if age<=25:
    print("sorry,due to your age there is no insurance plan for you")
else:
    employment=input("tell whether u are employed or unemployed")
    marital_status=input("are u married or unmarried")
    if 25<age<40 and employment=="unemployed" and marital_status=="unmarried":
                print("the insurance plan for you is 1400PKR/month")
    if 25<age<=40 and emloyment=="employed" and marital_status=="unmarried":
                print(" the insurance plan for you is 800PKR/month")
    if 25<age<=40 and employment=="employed" and marital_status=="married":
                print("the insurance plan for you is 1000PKR/month")
    if 25<age<=40 and employment=="unemployed" and marital_status=="married":
                print("the insurance plan for you is 1200PKR/month")
    if age>40:
                print("the insurance plan for you is 1500PKR/month")
                
    
        
        
