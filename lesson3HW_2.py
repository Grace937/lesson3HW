import random
v=random.randint(1,20)

i=1

g=int(input('Guess a number'))

while i<5:
    
    if g>v:
        print('Too large')
        g=int(input('Try again'))
        i=i+1

    elif g<v:
        print('Too Small')
        g=int(input('Try again'))
        i=i+1

    elif g==v:
        print('Correct!!!')
        print('You guess',i,'times')
        i=6
        
if i!=7:
    print('game over')