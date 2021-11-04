import random

def dice_roll():

    dice = random.randint(1,6)

    if dice==1:
        print('..................................')
        print('|                                 |')
        print('|                                 |')
        print('|                                 |')
        print('|                                 |')
        print('|               0                 |')
        print('|                                 |')
        print('|                                 |')
        print('|                                 |')
        print('|                                 |')
        print('..................................')
    
    if dice==2:
        print('..................................')
        print('|                                 |')
        print('|                                 |')
        print('|                                 |')
        print('|                                 |')
        print('|             0       0           |')
        print('|                                 |')
        print('|                                 |')
        print('|                                 |')
        print('|                                 |')
        print('..................................')

    if dice ==3:
        print('..................................')
        print('|                                 |')
        print('|                                 |')
        print('|      0                          |')
        print('|                                 |')
        print('|                0                |')
        print('|                                 |')
        print('|                                 |')
        print('|                           0     |')
        print('|                                 |')
        print('..................................')

    if dice==4:
        print('..................................')
        print('|                                 |')
        print('|        0               0        |')
        print('|                                 |')
        print('|                                 |')
        print('|                                 |')
        print('|                                 |')
        print('|                                 |')
        print('|        0               0        |')
        print('|                                 |')
        print('..................................')

    if dice==5:
        print('..................................')
        print('|                                 |')
        print('|        0               0        |')
        print('|                                 |')
        print('|                                 |')
        print('|                0                |')
        print('|                                 |')
        print('|                                 |')
        print('|        0               0        |')
        print('|                                 |')
        print('..................................')
    
    if dice==6:
        print('..................................')
        print('|                                 |')
        print('|        0               0        |')
        print('|                                 |')
        print('|                                 |')
        print('|        0               0        |')
        print('|                                 |')
        print('|                                 |')
        print('|        0               0        |')
        print('|                                 |')
        print('..................................')
    

# call the function

dice_roll()