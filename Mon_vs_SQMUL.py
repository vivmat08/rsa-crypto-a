import MontgomeryReduction
from random import randrange
# from timeit import default_timer as timer
from time import time
from RabinMiller import generate_prime_number
from datetime import timedelta

def SQMUL(base, power, modulo):
    
    if power == 1:
        return base

    if power % 2 == 0:
        half_prod = SQMUL(base, power // 2, modulo) % modulo
        return (half_prod * half_prod) % modulo

    else:
        half_prod = SQMUL(base, power // 2, modulo) % modulo
        return (((half_prod * half_prod) % modulo) * base) % modulo



def generate_randoms(default = 10000):
    randoms = []
    for _ in range(default):
        randoms.append(randrange(10**308, 10**309))

    return randoms


def multipleMontgomery(mr, randoms):
    for num in randoms:
        cval = mr.convert_in(num)
        m = mr.convert_out(mr.pow(cval,65537))

def multipleSQMUL(randoms, n):

    for num in randoms:
        m = SQMUL(num, 65537, n)


def main():

    array = generate_randoms()

    p = generate_prime_number(512)
    q = generate_prime_number(512)
    n = p * q
    
    mr = MontgomeryReduction.MontgomeryReducer(n)
    start = time()
    multipleMontgomery(mr, array)
    end = time()
    print((end - start))

    start = time()
    multipleSQMUL(array, n)
    end = time()
    print((end - start))


if __name__ == '__main__':
	main()

