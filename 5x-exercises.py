"""Think Python, chapter 5 exercises."""

import time


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


def check_print_method(a, b, c, n):
    """Takes inputs and outputs a string, ready to print."""
    return ("Trying " + str(a) + "^" + str(n) + " + " + str(b) + "^" +
            str(n) + " = " + str(c) + "^" + str(n))


a = 3
b = 7
c = 10
n = 5

print(check_print_method(a, b, c, n))
check_fermat(a, b, c, n)

a = 3
b = 5
c = 7
n = 4
print(check_print_method(a, b, c, n))
check_fermat(a, b, c, n)


print("\n\n5.3\n")
