# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 05:56:48 2024
Simple Fun Adventure Game
@author: Shannon
"""
#My first attempt at coding a game. It's simple, but it worked. I am happy
nick_name = input('Please enter your game name: ')
print(f"Welcome to the jungle, {nick_name}!")
reply = input('''You are stumbling through the jungle and can go Left or Right. Do you want to go left or right? ''').lower()

if reply == 'left':
    reply = input('You fall into a crocodile infested river, and you cannot swim. Do you sink or float? ')
    if reply == 'float':
        print('You floated down river right into a hippo')
    elif reply =='sink':
        print('You sank right down into the mouth of a giant whale')
    else:
        print('You are screwwd all around sucka')
elif reply == 'right':
    reply = input('''You've come to a broken, wobbly bridge.\nDo you dare try and cross or\ndo you sneak back
                  with your tail between your legs.\ntype cross or back? ''')
    if reply == 'cross':
        print("You are so chucked.There is a hungry mad lion waiting for you. Sad face")
    elif reply == 'back':
        reply = input('You cross the bridge and meet a stranger. Do you knock them over(yes/no? ')
        if reply == 'yes':
            print('You talk to the stranger and they throw you over the bridge')
        elif reply == 'no':
            print('You shoot the stranger and keep your sad life')
        else:
            print('Not what I asked you stubborn jackass')
else:
    print('Not a valid answer id-git')
print("The struggle is real....")





