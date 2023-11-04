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

def main():
    # Taking parameters for selecting prime numbers
    # Taking message as a numerical value for encryption
    a = int(input("Enter lower bound of the interval: "))
    b = int(input("Enter upper bound of the interval: "))
    msg = int(input("Enter message for encryption: "))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

