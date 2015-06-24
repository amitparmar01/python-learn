
def main():

	num = int(input('Please enter a number: '))

	numbers = range(1, num + 1)
	divisors = []

	for number in numbers:
		if num % number == 0:
			divisors.append(number)

	print(divisors)




if __name__ == "__main__":
	main()
