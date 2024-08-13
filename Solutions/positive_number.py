# get a positive number from the user
# keep asking until the user complies
num = int(input("Enter a number greater than 0: "))

while num < 1: # keep going as long as num is NOT >= 1
    print('Sorry! The number must be >= 0!')
    num = int(input("Enter a positive number: "))
