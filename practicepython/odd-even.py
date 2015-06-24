
def main():

	num = int(input('Please enter a number: '))

	if num % 2 == 0:
		print('This is an even number!')
		
		if num % 4 == 0:
			print('Also, it is a multiple of 4!')
	else:
		print('This is an odd number!')

	num =  int(input('Please enter a number: '))
	check =  int(input('Please enter an another number: '))

	if num % check == 0:
		print(str(check) + ' divides evenly into ' + str(num))
	else:
		print(str(check) + ' does not divide evenly into ' + str(num))


if __name__ == "__main__":
	main()
