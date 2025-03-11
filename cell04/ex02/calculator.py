num1 = float(input("emter first number: "))
num2 = float(input("enter the second number: "))
additon = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
if num2 != 0:   
    division = num1 / num2
else:
    division = "Undefrined (Cannot division by zero)"
print(f"{num1} + {num2} = {additon}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")