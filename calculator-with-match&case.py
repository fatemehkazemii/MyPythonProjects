a = int(input('Enter a number :'))
b = int(input('Enter a number :'))
c = input('Enter a sign :')



match c:
    case ('+'):
        print(a + b)
    case ('-'):
        print(a - b)
    case ('/'):
        print(a / b)
    case('*'):
        print(a * b)
        

    
    