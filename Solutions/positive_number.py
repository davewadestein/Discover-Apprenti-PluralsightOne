# get a positive number from the user
# keep asking until the user complies
num = 0 # "priming the pump"

while num < 1: # keep going as long as num is NOT >= 1
    num = int(input("Enter a positive number: "))
    if num < 1:
        print('The number needs to be >= 1')
