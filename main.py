import random
import math

def p_numbers(a, b):
    prime_list = []
    for i in range(max(2, a), b + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)

    # Checking that the range has at least 2 prime numbers between them
    if len(prime_list) < 2:
        raise ValueError("There are not enough prime numbers in the specified range.")
    # Select 2 prime numbers randomly from the range
    p, q = random.sample(prime_list, 2)
    n = p * q
    return n

def main():
    # Taking parameters for selecting prime numbers
    # Taking message as a numerical value for encryption
    a = int(input("Enter lower bound of the interval: "))
    b = int(input("Enter upper bound of the interval: "))
    msg = int(input("Enter message for encryption: "))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

