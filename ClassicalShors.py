import numpy
import math
import random

#check if a value is a prime number or not
def prime(value):
    bool = True
    if value >= 2:
        for i in range(2, value):
            if (value % i) == 0:
                bool = False
                break
            else:
                bool = True

    return bool

#checks if value can be written in the form of x^a
def power(value):
    bool = True

    if value <= 1:
        bool = True

    for x in range(2, (int)(math.sqrt(value))+1):
        exp = x
        while exp <= value:
            exp = exp * x

            if exp == value:
                bool = True
                break

            else:
                bool = False
    
    return bool

#Shors factoring algorithm
def Shors(value):
    factors = 0,0
    if prime(value) == True:
        factors = value, 1

    elif (value % 2) == 0:
        factors = value/2, 2

    elif power(value) == True:
        factors = 0,0

    else:
        for x in range(1, (int)(math.sqrt(value))):
            if math.gcd(x, value) != 1:
                factors = x, math.gcd(x, value)

            else:
                r = ClassicalPeriod(x, value)
                if r % 2 == 0:
                    factors = math.gcd((int)(x**(r/2)-1)%value, value), math.gcd((int)(x**(r/2)+1)%value, value)

                else:
                    continue
    return factors


def periodFunction(x, r):
    return 
#the classical function for period finding as opposed to its
#quantum counterpart
def ClassicalPeriod(x, value):
    target = 0

    for r in range(1, value):
        if (x**r) == 1 % value:
            target = r
        else:
            continue
    return target

print(prime(15))
print(Shors(15))
print(ClassicalPeriod(3,15))

