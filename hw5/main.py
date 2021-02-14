"""
pirple/python/hw5/main.py
Homework Assignment #5

Fizz Buzz -- print the numbers 1-100, but for multiples of
 3 print "Fizz" instead.  For multiples of 5, print "Buzz"
 instead. And for multiples of both, print "FizzBuzz". If
 the number is prime, print "Prime"
"""

def divisible_by_3(number):
    if number%3 == 0:
        return True
    else:
        return False


def divisible_by_5(number):
    if number%5 == 0:
        return True
    else:
        return False


def is_prime(number, divisors):
    prime = True
    for d in divisors:
        if number%d == 0:
            if d != 1 and number != d:
                prime = False
                break
    return prime

divisors = []

for i in range(1,101):
    divisors.append(i)

    div3  = divisible_by_3(i)
    div5  = divisible_by_5(i)
    prime = is_prime(i, divisors)

    print(str(i) + '\t', end='')
    if prime:
        print('Prime')
    elif (div3 and div5):
        print('FizzBuzz')
    elif div3:
        print('Fizz')
    elif div5:
        print('Buzz')
    else:
        print()
