#-----------Day1-----------------#
#learning python from scratch 

first_number = int(input("Enter First Number:"))
second_number = int(input("Enter Second Number:"))
print("List of operator : \n 1. + \n 2. - \n 3. * \n 4. /")
operation = input("Enter operation, you wanna perform on your input:")

if(operation == "+"):
    print(f"The sum of your two number =  {first_number + second_number}")
elif(operation == "-"):
     print(f"The substraction of your two number =  {first_number - second_number}")
elif(operation == "*"):
     print(f"The multiplication of your two number =  {first_number * second_number}")
elif(operation == "/"):
     print(f"The division of your two number =  {first_number / second_number}")
else:
     print("Enter Correct operation from above.! Thanks")