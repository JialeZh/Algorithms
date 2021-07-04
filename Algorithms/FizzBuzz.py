
# number % 3, print fizz
# number % 5, print Buzz
# number % 3 and 5, print FizzBuzz

"""number = 0
while number <= 100:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        number = number + 1
    elif  number % 3 == 0:
        print("Fizz")
        number = number + 1
    elif number % 5 == 0:
        print("Buzz")
        number = number+ 1
    else:
        print(number)
        number = number +  1
"""


for number in range(100):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif  number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
