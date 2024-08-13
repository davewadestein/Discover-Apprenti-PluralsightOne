import random # 1 (load random module, i.e., make it so we can use it)
number = random.randint(1, 100) # also 1 (get a random number between 1 and 100)
guess = 0 # 1a, prime the pump

while guess != number: # 1a (while user's guess does not match our number)
    guess = int(input('Your guess? ')) # 2, 2a (get guess and covert to int)
    if guess > number: # 3
        print('Too high!') # 3a
    elif guess < number: # 4
        print('Too low!') # 4a
    else:
        print('You got it!')
