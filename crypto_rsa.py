from Crypto.Util.number import bytes_to_long 
from Crypto.Util.number import long_to_bytes
from random import randrange
from RabinMiller import generate_prime_number


def lcm(num1: int, num2: int) -> int:
	return (num1 * num2) // gcd(num1, num2)

def gcd(num1: int, num2: int) -> int:
	if num1 == 0:
		return num2
	else:
		return gcd(num2 % num1, num1)


def extended_gcd(num1: int, num2: int):
	old_r, r = num1, num2
	old_s, s = 1, 0
	old_t, t = 0, 1

	while (r != 0):
		quotient = old_r // r
		old_r, r = r, old_r - quotient * r
		old_s, s = s, old_s - quotient * s 
		old_t, t = t, old_t - quotient * t

	return old_s, old_t

def mul_inverse(num1: int, num2: int) -> int:
	s, t = extended_gcd(num1, num2)
	return s % num2


def encrpytRSA(m: int, bits: int):

	# p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
	# q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
	p = generate_prime_number(bits)
	q = generate_prime_number(bits)
	
	n = p * q


	# Find carmichael totient of n, which is lcm(p - 1, q - 1)
	carmichael_totient = lcm(p - 1, q - 1)
	
	# Choose an exponent such that gcd(e, carmichael totient) is 1
	e = 65537
	while gcd(e, carmichael_totient) != 1:
		e = randrange(3, carmichael_totient, 2)
	

	d = mul_inverse(e, carmichael_totient)

	c = pow(m, e, n)
	return n, e, c, d



def decryptRSA(c: int, d: int, n: int):

	m = pow(c, d, n)
	return m


def main():

	file = open("encrypt.txt", "r")
	plaintext = bytes(file.read(), 'utf-8')
	file.close()
	m = bytes_to_long(plaintext)

	print(f"m = {m}")

	n, e, c, d = encrpytRSA(m, 512)
	print(f"Public key:\n(n, e) = ({n}, {e})")
	print(f"Ciphertext = {c}")
	plaintext_decrypted = str(long_to_bytes(decryptRSA(c, d, n)), encoding = "utf-8")
	print(f"Plaintext\n{plaintext_decrypted}")



if __name__ == '__main__':
	main()