#question 1
# print("Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are")

#question 2
# first= input("ENTER FIRST NAME \n")
# last= input("ENTER LAST NAME \n")
# print(last," ",first)

#question 3
# n=int(input("ENTER RADIUS OF CIRCLE \n"))
# area = 3.14*n*n
# print("AREA : ",area)

#question 4
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[3])

n=input("ENTER VALUE OF N \n")
nn=n+n
nnn=n+n+n
n=int(n)
nn=int(nn)
nnn=int(nnn)
sum=n+nn+nnn
print("VALUE : ",sum)

#question7
temp=int(input("ENTER CELSIUS \n"))
temp=(n*1.8)+32
print("FEHRENHEIT : ",temp)

#question 8
n1=int(input("ENTER FIRST NUMEBR"))
n2=int(input("ENTER SECOND NUMEBR"))
temp=n1
n1=n2
n2=temp
print("n1 : ",n1)
print("n2 : ",n2)

#question 9
n=int(input("ENTER NUMBER \n"))
if n%2==0 :
    print("NUMBER IS EVEN \n")
else:
    print("NUMBER IS ODD")

#question 10
yr=int(input("ENTER YEAR \n"))
if yr%4 ==0 :
    print("YEAR IS LEAP \n")
else:
    print("YEAR IS NOT LEAP")

#question 11
import math
x1=int(input("ENTER x1 \n"))
y1=int(input("ENTER y1 \n"))
x2=int(input("ENTER x2 \n"))
y2=int(input("ENTER y2 \n"))
dist=math.sqrt((y2-y1)+(x2-x1))
print("DISTANCE : ",dist)

#question 12
a1=int(input("ENTER ANGLE 1"))
a2=int(input("ENTER ANGLE 2"))
a3=int(input("ENTER ANGLE 3"))
if a1+a2+a3==180:
    print("IT CAN FORM A TRIANGLE")
else:
    print("IT CANNOT FORM A TRIANGLE")

#question 13
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))
n = int(input("Enter the number of times interest is compounded per year (e.g., 1 for annually, 4 for quarterly, 12 for monthly): "))
time = float(input("Enter the number of years the money will be invested: "))
future_value = principal * (1 + rate / n)**(n * time)
compound_interest = future_value - principal
print(f"\nFuture Value (including interest): {future_value:.2f}")
print(f"Total Compound Interest: {compound_interest:.2f}")

#question 14
number=int(input("ENTER THE NUMBER \n"))
flag=0
for i in range(2,number):
    if number%i==0:
        flag=1
    else:
        None
if flag==0:
    print("IT IS PRIME")
else:
    print("IT IS NOT PRIME")

#question 15
n=int(input("ENTER THE NUMBER \n"))
sum=0
for i in range(1,n+1):
    sum=sum+(i*i)
print("sum : ",sum)