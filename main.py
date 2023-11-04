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
    return n, prime_list
# A simple method to evaluate Euler's Totient Function
def phi(n):
    result = 1
    for i in range(2, n):
        if math.gcd(i, n) == 1:
            result += 1
    return result

# Public key
def public_key(n, m):
    phi_n = phi(n)
    e = random.choice([e for e in range(2, phi_n) if math.gcd(e, phi_n) == 1])
    c = pow(m, e, n)
    return e, n, c

# Private Key
def private_key(c, e, n):
    phi_n = phi(n)
    for k in range(1, phi_n):
        if (k * e) % phi_n == 1:
            d = k
            break
    m = pow(c, d, n)
    return d, n, m

def main():
    # Taking parameters for selecting prime numbers
    # Taking message as a numerical value for encryption
    a = int(input("Enter lower bound of the interval: "))
    b = int(input("Enter upper bound of the interval: "))
    msg = int(input("Enter message for encryption: "))
    # Calling prime number generator function
    n = p_numbers(a, b)
    #Calling Public and Private key functions
    e, n, c = public_key(n, msg)
    d, n, m = private_key(c, e, n)
    # Displaying the Encrypted and Decrypted Message
    print("After encryption, the ciphertext is:", c)
    print("After decryption, the plaintext is:", m)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

