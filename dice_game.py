# import random
# a = random.randint(1,6)
# print(a)
# if a == 6 :
#     print('YOU WIN!!')
# else:
#     print('try again...')
    
#################################################################
#With input

import random
while True:
    a = int(input('Roll the dice:'))
    x = random.randint(1, 6)
    if x == a :
        print('you win')
        break
    else:
        print('try again')

