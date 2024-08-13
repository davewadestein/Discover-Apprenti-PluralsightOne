# 1. prompt for integer / input integer
# 1a. result = 1, holds our running total
# 2. for each number from 2..integer: # 1..5
# 3.     multiply result by number, then put that back into result

factorial = int(input('Enter a number: ')) # 1 (+ int-ify)
result = 1 # 1a

# we must add 1 for Dijkstra
for number in range(2, factorial + 1): # 2
    print(f'result is {result}, multiply by {number}')
    result = result * number # 3
    # result *= number is shorthand for above

print(result)
