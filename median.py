"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

print(numbers)
    
def find_median(numbers):
    n = len(numbers)

    if(n%2 == 1):
        median = numbers[n//2]
    else:
        x = numbers[(n-1)//2]
        y = numbers[n//2]
        median = (x+y)/2
    return median

median = find_median(numbers)
print('Median:', median)
