import random

user_name = str(input('Enter your name: '))
print(f'Welcome to the higher/lower game, {user_name}!')

lower_bound = int(input('Enter the lower bound: '))
upper_bound = int(input('Enter the upper bound: '))


if lower_bound < upper_bound:
  secret_num = random.randint(lower_bound, upper_bound)    
  user_guess = int(input(f'Great, now guess a number between {lower_bound} and {upper_bound}: '))
  while user_guess != secret_num:
    if user_guess < secret_num:
      print('Nope, too low., \n')
      user_guess = int(input(f'Guess another number: '))
      continue
    elif user_guess > secret_num:
      print('Nope, too high., \n')
      user_guess = int(input(f'Guess another number: '))
      continue
  else:
    print('You got it!')
else:
  print('The lower bound must be less than the upper bound.')
