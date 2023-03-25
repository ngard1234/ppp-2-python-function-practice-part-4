# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(num, begin, end):
    if num == begin:
        return print(f'Your number {num} is equal to the beginning number. Please enter another number')
    elif num == end:
        return print(f'Your number {num} is equal to end number. Please enter another number')
    elif num >begin and num < end:
        return True, print(f'Your number {num} is between {begin} and {end}')
    else:
        return False, print(f'Your number {num} is not between {begin} and {end}')


num_within(3 , 9, 12)
num_within(2, 1, 3)
num_within(10, 2, 5)
num_within(10, 2, 10)