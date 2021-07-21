import random
v=random.randint(1,10)
g=int(input('猜一個數字?'))
while g!=v:
   g=int(input('再猜一次'))
if g==v:
    print('猜對了!')