def main():

    word = input('Please enter a word: ')
    lengthWord = len(word)

    reverseWord = ''

    for i in range(len(word)):
        reverseWord += word[lengthWord - 1]
        lengthWord -= 1

    if word == reverseWord:
        print('This is a palindrome!!!')
    else:
        print('This is not a palindrome!')


if __name__ == "__main__":
	main()
