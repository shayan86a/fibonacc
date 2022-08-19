x = int(input(":"))
num1 = 0
num2 = 1
while num1 < x or num2 < x:
    print(num1, ", ", end="")
    num1 = num1 + num2
    print(num2, ", ", end="")
    num2 = num1 + num2
    
