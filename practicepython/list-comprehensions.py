def main():

	a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

	even = [num for num in a if num%2 == 0]

	print(even)


if __name__ == "__main__":
	main()
