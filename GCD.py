number1 = int(input('Enter a number:'))
number2 = int(input('Enter a number:'))
GCD = 1

if number1 > number2:
    number1 , number2 = number2 , number1
    
for i in range(1 , number1+1):
    if number1 % i == 0 and number2 % i == 0:
        GCD = i 

print(GCD)
