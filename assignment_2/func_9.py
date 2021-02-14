def is_prime(num):
    if num == 1:
        print("Neither prime nor composite")
    else:
        divisors = [i for i in range(1, num) if num % i == 0]
        if len(divisors) > 1:
            print("Not a prime")
        else:
            print("Prime Number")


is_prime(2)
is_prime(1)
is_prime(7)
is_prime(8)
