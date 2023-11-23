#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i=11
    while i>0:
       i-=1
       print(i)
    
    if(i==0):
            print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    squared_numbers=list()
    for number in int_list:
        squared_number=number**2
        squared_numbers.append(squared_number)
    
    return squared_numbers
    pass

def fizzbuzz():
    # code goes here!
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
    pass
