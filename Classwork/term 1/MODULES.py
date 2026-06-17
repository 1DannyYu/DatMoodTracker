import random

line = input('Dice roll!')

while line != 'x':
    line = input(random.randrange(1,7))
