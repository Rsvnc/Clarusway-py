# Task : Print the Fizz Buzz numbers.

# Fizz Buzz is a famous code challenge used in interviews to test basic programming skills. It's time to write your own implementation.
# Print numbers from 1 to 100 inclusively following these instructions:
# if a number is multiple of 3, print "Fizz" instead of this number,
# if a number is multiple of 5, print "Buzz" instead of this number,
# for numbers that are multiples of both 3 and 5, print "FizzBuzz",
# print the rest of the numbers unchanged.
# Output each value on a separate line.







for num in range(1,101):
  if num%3==0 and num%5==0:
    print("Fizz Buzz")
  elif num%3==0:
    print("Fizz")
  elif num%5==0:
    print("Buzz")
  else:
    print(num)
    
    
    
    
