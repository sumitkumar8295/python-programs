number1= int(input("enter the first number"))
number2= int(input("enter the second number"))
number3=int(input("enter the third number"))
number4=int(input("enter the fourth number"))


if number1 > number2 and number1 > number3 and number1 > number4 :
    print("number1 is the largest number")
elif  number2 > number3 and number2 > number4 :
    print("number2 is the greatest number")
elif number3 > number4 :
    print("number3 is the greatest number")
else:
    print("number 4 is the greatest number"