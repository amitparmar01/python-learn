
import random

def get_random_num():
	return random.randint(1,9)

def main():

	playedTimes = 0

	while 1:

		aiGuess = get_random_num()

		userGuess = input('Please guess a number between 1 & 9 or type exit to quit: ')

		if userGuess == 'exit':
			break
		else:
			userGuess = int(userGuess)		

		if aiGuess == userGuess:
			print('It is exactly same!')
		elif abs(userGuess - aiGuess) == 1:
			print('You were very close!! AI chose:', str(aiGuess) )
		elif abs(userGuess - aiGuess) == 2:
			print('You were close! AI chose:', str(aiGuess))
		elif abs(userGuess - aiGuess) > 2 and userGuess < aiGuess:
			print('You guessed too low! AI chose:', str(aiGuess))
		elif abs(userGuess - aiGuess) > 2 and userGuess > aiGuess:
			print('You guessed too high! AI chose:', str(aiGuess))

		playedTimes += 1

	print('\n\nThanks for playing. You played '+ str(playedTimes) + ' times!')



if __name__ == "__main__":
	main()
