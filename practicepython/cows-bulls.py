
import random
def generate_random_4_digits():

	digits = []

	while True:
		digit = random.randint(0,9)
		if not digit in digits:
			digits.append(digit)

		if digits[0] == 0:
			digits.remove(0)

		if len(digits) == 4:
			break;

	return digits

def main():


	aiNumber = generate_random_4_digits()

	playedTimes = 0

	#print(aiNumber)

	while True:

		bulls = []
		commonDigits = []
		cows = []
		
		userGuessStr = input('Please enter a 4 digit number: ')

		userGuess = [int(x) for x in userGuessStr]

		#print('User:', userGuess)

		commonDigits = [digit for digit in userGuess if digit in aiNumber]

		#print('Common: ', commonDigits)

		bulls = [aiNumber[i] for i in range(4) if aiNumber[i] == userGuess[i]]

		#print('Bulls: ', bulls)

		cows = [digit for digit in commonDigits if not digit in bulls]

		#print('Cows: ', cows)

		print ('Cows: %d | Bulls: %d' % (len(cows), len(bulls)))

		playedTimes += 1

		if len(bulls) == 4:
			print('\n\nYou win after %d tries!!!' % playedTimes)
			break;


if __name__ == "__main__":
	main()
