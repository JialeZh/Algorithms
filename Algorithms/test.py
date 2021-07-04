List = []
def fizzBuzz(self, n):
    for i in range(n):
         if i % 3 == 0 and i % 5 == 0:
            List.append("FizzBuzz")
        elif i % 3 == 0:
            List.append("Fizz")
        elif i % 5 == 0:
            List.append("Buzz")
        else:
            List.append(i)

print(fizzBuzz())