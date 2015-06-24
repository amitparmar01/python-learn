
def fibonacci(num):

	if num == 0:
		return 0
	elif num == 1:
		return 1

	fSum = fibonacci(num-1) + fibonacci(num-2)

	return fSum


def main():

	length = int(input('How many fibonacci numbers to generate? '))

	series = []
	total = 0
	
	for i in range(length + 1):
		series.append(fibonacci(i))

	print('Series :')
	print(series)

	for num in series:
		total += num

	print('\nSeries Total: ' + str(total))


if __name__ == "__main__":
	main()
