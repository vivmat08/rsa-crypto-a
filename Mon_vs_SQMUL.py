import MontgomeryReduction
from random import randrange
from timeit import default_timer as timer
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



def generate_randoms(default = 1000):
    randoms = []
    for i in range(default):
        randoms.append(randrange(10**500, 10**502))

    return randoms


def multipleMontgomery(randoms, n):
    mr = MontgomeryReduction.MontgomeryReducer(n)
    for num in randoms:
        cval = mr.convert_in(num)
        m = mr.convert_out(mr.pow(cval,65537))

def multipleSQMUL(randoms, n):

    for num in randoms:
        m = SQMUL(num, 65537, n)

def multiplePow(randoms, n):

    for num in randoms:
        m = pow(num, 65537, n)


def main():

    array = generate_randoms()

    p = generate_prime_number(1024)
    q = generate_prime_number(1024)
    n = p * q
    
    start = timer()
    multipleMontgomery(array, n)
    end = timer()
    print((end - start))

    start = timer()
    multipleSQMUL(array, n)
    end = timer()
    print((end - start))


    start = timer()
    multiplePow(array, n)
    end = timer()
    print((end - start))


if __name__ == '__main__':
	main()

