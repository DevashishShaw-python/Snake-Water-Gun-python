import random
a = ['snake', 'water', 'gun']
c = random.choice(a)
b = input('enter your choice : snake, water or gun ')
u = b.lower()
print(f"player choose = {u}" )
print(f"computer choose = {c}")
if ((u) == (c)):
    print('Its a draw')
elif ((u) == 'snake' and (c) == 'water'):
    print('player wins')
elif ((u) == 'snake' and (c) == 'gun'):
    print('computer wins')
elif ((u) == 'water' and (c) == 'snake'):
    print('computer wins')
elif ((u) == 'water' and (c) == 'gun'):
    print('player wins')
elif ((u) == 'gun' and (c) == 'snake'):
    print('player wins')
elif ((u) == 'gun' and (c) == 'water'):
    print('computer wins')
else:
    print(' Incorrect choice !! \nchoose only from the provided option')
