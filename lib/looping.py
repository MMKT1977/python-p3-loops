#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i=10
    while i>0:
        print(i)
        i -=1
    print("Happy New Year!")
happy_new_year()

def square_integers(int_list):
    # code goes here!
    squared_list = [num ** 2 for num in int_list]
    return squared_list
square_integers([1,2,3,4,5])

def fizzbuzz():
    # code goes here!
    for num in range(1,101):
        if num % 3 == 0 and num % 5 ==0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
fizzbuzz()
