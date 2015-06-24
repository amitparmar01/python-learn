
import random

def ai_selection():
	return random.randint(1,3)

def main():

	rock = 1
	paper = 2
	scissors = 3

	while 1:

		userSelection = int(input('Enter your option: 1 for Rock, 2 for Paper, and 3 for Scissors: '))

		aiSelection = ai_selection()

		print('AI selected:', aiSelection)

		#print(userSelection, aiSelection)

		if userSelection == rock and aiSelection == scissors:
			print('You win!!!')
		elif userSelection == paper and aiSelection == rock:
			print('You win!!!')
		elif userSelection == scissors and aiSelection == paper:
			print('You win!!!')
		elif userSelection == scissors and aiSelection == rock:
			print('You lose!!!')
		elif userSelection == rock and aiSelection == paper:
			print('You lose!!!')
		elif userSelection == paper and aiSelection == scissors:
			print('You lose!!!')
		else:
			print('Drawwww!!!')


		replay = input('\nDo you want to play again? yes or no: ')

		if replay.lower() == 'yes' or replay.lower() == 'y':
			continue
		else:
			break

if __name__ == "__main__":
	main()
