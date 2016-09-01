import sys
import time

def secret(n):
	return n+n

def primes_of(n):
	"""Uses sieve of Eratosthenes to list prime numbers below input n
	Args:
		n: Maximum integer representing 
	Returns:
		An array containing all prime numbers below n
	Alternative:
		Pyprimesieve https://github.com/jaredks/pyprimesieve
	"""
	if n < 2:
		return None

	sieve = {i:True for i in range(2,n+1)}

	for j in range(2, n+1):
		if sieve[j] == True:
			m = 2
			while j*m <= n:
				sieve[j*m] = False
				m+=1

	return [x for x,y in sieve.items() if y == True]


def is_additive(primes):
	"""Checks if secret(x+y) == secret(x) + secret(y) given x,y are prime numbers below n
	"""

	# Null Check
	if primes == None:
		return "No prime numbers below your input exist"

	f1 = [secret(x)+secret(y) for x in primes for y in primes]
	f2 = [secret(x+y) for x in primes for y in primes]

	return f1 == f2


if __name__ == "__main__":
	# Check argument type
	try:
		number = int(sys.argv[1])
		start = time.time()
		print is_additive(primes_of(number))

		end = time.time()
		print "elapsed %ss" % str(end-start)
		
	except ValueError:
		print("Only integer type is accepted")