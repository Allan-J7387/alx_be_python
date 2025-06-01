FirstNumber = int(input("Enter the first number: "))
SecondNumber = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

if operation == "+":
    result = FirstNumber + SecondNumber
elif operation == "-":
    result = FirstNumber - SecondNumber
elif operation == "*":
    result = FirstNumber * SecondNumber
elif operation == "/":
    if SecondNumber != 0:
        result = FirstNumber / SecondNumber
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operation"


print(str(result))
