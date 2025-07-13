weight = float(input('Enter your weight:'))
height = float(input('Enter your height:'))
bmi = weight / height**2
print('Your bmi is' , bmi)

if bmi < 18.5:
    print('Under weight')
    
elif 18.5 <= bmi <= 24.9:
    print('Normal weight') 

elif 25 <= bmi <= 29.9:
    print('Over weight')
    
elif 30 <= bmi <= 39.9:
    print('Obese')

elif bmi > 40:
    print('Extremely obesity')