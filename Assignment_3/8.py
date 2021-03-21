# # 8. Write a function, is_prime, that takes an integer and returns True if thenumber is prime and False if the
# number is not prime.

def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif not number & 1:
        return False

    for n in range(3, int(number ** 0.5) + 1, 2):
        if number % n == 0:
            return False

    return True


print(1, "is prime", is_prime(1))
print(2, "is prime", is_prime(2))
print(3, "is prime", is_prime(7))
print(29, "is prime", is_prime(29))
