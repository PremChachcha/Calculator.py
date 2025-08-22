def arithmetic_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    modulus = num1 % num2 if num2 != 0 else "Cannot perform modulus with zero"

    return addition, subtraction, multiplication, division, modulus

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

results = arithmetic_operations(num1, num2)
print("Addition:", results[0])
print("Subtraction:", results[1])
print("Multiplication:", results[2])
print("Division:", results[3])
print("Modulus:", results[4])
