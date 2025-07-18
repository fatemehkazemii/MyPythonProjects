import random
a = random.randint(1,100)
c = 0
while True:
    b = int(input('guess a number : '))
    
    if a == b:
        break
    elif a > b :
        print('guess a bigger one!')
        c += 1
    elif a < b :
        print('guess a smaller one!')
        c+=1
    else:
        print('Error')
        
print('you win after' , c , 'tries' , chr(3))


