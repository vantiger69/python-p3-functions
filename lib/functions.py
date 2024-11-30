#!/usr/bin/env python3

def greet_programmer():
    pass
print("Hello,programmer!")

def greet(name):
    print(f"Hello,{name}!")
    pass
greet("Van")



def greet_with_default(name="Van"):
    print(f"Hello,{name}")
    pass
greet_with_default()



def add(num1, num2):

    return num1 + num2
    pass 
result = add(1,2)
print("The sum is:",result)



def halve(number):
    if type(number) not in [int,float]:
        return None
    return number / 2
print(halve(12))
  