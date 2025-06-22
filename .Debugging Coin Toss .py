print("Name   : prajwal br")
 print("USN    : 1AY24AI083")
 print("Section: O")
 import random
 output 
guess = ''
 while guess not in ('heads', 'tails'):
 print('Guess the coin toss! Enter heads or tails:')
 guess = input()
 toss = 'heads' if random.randint(0, 1) == 1 else 'tails'
 if toss == guess:
 print('You got it!')
 else:
 print('Nope! Guess again!')
 guess = input()
 if toss == guess:
 print('You got it!')
 else:
 print('Nope. You are really bad at this game.')
