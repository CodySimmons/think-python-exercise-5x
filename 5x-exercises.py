"""Think Python, chapter 5 exercises."""

import time
import turtle


print("5.1\n")


def zero_checker(var):
    """Takes int variable, returns string with leading 0 if int is below 10."""
    if (var < 10):
        return str("0"+str(var))
    else:
        return str(var)


current_seconds = zero_checker(int(time.time() % 60))
current_mintues = zero_checker(int(time.time() / 60 % 60))
current_hour = zero_checker(int(time.time() / 60 / 60 % 24))
print(current_hour + ":" + current_mintues + ":" + current_seconds + " GMT")


minutes_since_epoch = time.time() / 60.0
hours_since_epoch = minutes_since_epoch / 60.0
days_since_epoch = int(hours_since_epoch / 24.0)
print(str(days_since_epoch) + " days since epoch.")


print("\n\n5.2\n")


def check_fermat(a, b, c, n):
    """Check if Fermat's Last Theorem is correct."""
    if (n <= 2):
        print("n is not greater than 2")
    else:
        temp_sum = a**n + b**n
        if (temp_sum == c**n):
            print("Fermat was wrong.")
        else:
            print("No, doesn't work.")


def check_square_print_method(a, b, c, n):
    """Takes inputs and outputs a string, ready to print."""
    return ("Trying " + str(a) + "^" + str(n) + " + " + str(b) + "^" +
            str(n) + " = " + str(c) + "^" + str(n))


a = 3
b = 7
c = 10
n = 5

print(check_square_print_method(a, b, c, n))
check_fermat(a, b, c, n)

a = 3
b = 5
c = 7
n = 4
print(check_square_print_method(a, b, c, n))
check_fermat(a, b, c, n)


print("\n\n5.3\n")


def is_triangle(a, b, c):
    if ((c > a + b) or (b > a + c) or (a > b + c)):
        return "No"
    else:
        return "Yes"


def check_print_method(a, b, c):
    return ("Trying " + str(a) + " & " + str(b) + " & " + str(c))


a = 1  # input("Enter 3 sides of the triangle.\na = ")
b = 1  # input("b = ")
c = 12  # input("c = ")



print(check_print_method(a, b, c) + ". Is a trangle? " + is_triangle(a, b, c))


print("\n\n5.4\n")


def recurse(n, s):
    """
    Receives inputs from method input. Adds n to the total sum, s and reduces
    n by one until n reaches 0.
    """
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)


recurse(3, 0)


print("\n\n5.5\n")


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)


bob = turtle.Turtle()

bob.pu()
bob.goto(-150, 90)
bob.pd()
snowflake(bob, 300)
