import random
import math

# A simple method to evaluate Euler's Totient Function
def phi(n):
    result = 1
    for i in range(2, n):
        if math.gcd(i, n) == 1:
            result += 1
    return result

def main():
    # Taking parameters for selecting prime numbers
    # Taking message as a numerical value for encryption
    a = int(input("Enter lower bound of the interval: "))
    b = int(input("Enter upper bound of the interval: "))
    msg = int(input("Enter message for encryption: "))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

