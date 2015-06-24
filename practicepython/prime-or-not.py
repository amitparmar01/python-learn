
import random

def isThisPrime(prime):

	testNumbers = range(2, prime)

	for number in testNumbers:
		if prime % number == 0:
			return False

	return True		


def main():

	prime = int(input('Please enter a number to check for primality: '))

	if isThisPrime(prime):
		print('This is a prime number!!!')
	else:
		print('This is not a prime number.')


if __name__ == "__main__":
	main()
