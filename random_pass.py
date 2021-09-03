import string
import random

digit_number = int(input("how many digits do you want your password have"))
lower_number = int(input("how many lower_case do you want your password have"))
upper_number = int(input("how many upper_case do you want your password have"))
special_number = int(input("how many special_case do you want your password have"))


if digit_number > 0:
    dig = ''.join(random.choice(string.digits) for i in range(digit_number))
else:
    dig = ""
if lower_number > 0:
    lower = ''.join(random.choice(string.ascii_lowercase) for i in range(lower_number))
else:
    lower = ""
if upper_number > 0:
    upper = ''.join(random.choice(string.ascii_uppercase) for i in range(upper_number))
else:
    upper = ""
if special_number > 0:
    punctuation = ''.join(random.choice(string.punctuation) for i in range(special_number))
else:
    punctuation = ""
print(dig)
print(lower)
print(upper)
print(punctuation)


def password_generator():
    a = "".join(random.choice(dig) for i in range(digit_number))
    b = "".join(random.choice(lower) for i in range(lower_number))
    c = "".join(random.choice(upper) for i in range(upper_number))
    d = "".join(random.choice(punctuation) for i in range(special_number))
    x = "".join(list(a) + list(b) + list(c) + list(d))
    x = list(x)
    print(x)
    random.shuffle(x)
    print(x)
    print("".join(x))


print(password_generator())
