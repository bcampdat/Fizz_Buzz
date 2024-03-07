# FIZZBUZZ

"""
Write a program that prints the numbers from 1 to 100. 
But for multiples of 3 it prints "Fizz"instead of the 
number and for the multiples of five it prints "Buzz". For  
the numbers which are multiples of both 5 and 3 then you're going to print out 
"FizzBuzz"

"""
# funciones
# loopings
# Conditionals
# Math operators


# FizzBuzz
def fizzbuzz(max_value):
    for e in range(0, max_value + 1):
    
        if e % 3 == 0 and e % 5 == 0:
            print("FizzBuzz")
        elif e % 3 == 0:
            print("Fizz")
        elif e % 5 == 0:
            print("Buzz")
        else:
            print(e)

fizzbuzz(15)
