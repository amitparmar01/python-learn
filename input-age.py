def main():

	name = input('Please enter your name: ')

	age = int(input('Now enter your age: '))

	if age > 100:
		cent = age - 100
		year100th = 2015 - cent
		print('Hello, ' + name + '. You turned 100 in the year ' + str(year100th))	
	else:
		cent = 100 - age 
		year100th = 2015 + cent
		print('Hello, ' + name + '. You will be turning 100 in the year ' + str(year100th))	


if __name__ == "__main__":
	main()
