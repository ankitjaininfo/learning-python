number1=float(input("enter number1: "))
number2=float(input("enter number2: "))
arithmeticoperation=input("enter arithmeticoperations (/ * + -): ")
divison=number1/number2
multiplication=number1*number2
addition=number1+number2
subraction=number1-number2
if arithmeticoperation == "/":
	print("divison is",divison)
elif arithmeticoperation == "*":
	print("multiplicaton is",multiplication)
elif arithmeticoperation == "+":
	print("addition is",addition)
elif arithmeticoperation == "-":
	print("subraction is",subraction)
else:
	print("wrong Arithmetic Operation try again :( ")	