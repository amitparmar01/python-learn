
def main():
	
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  	c =[]

  	for item in b:
  		if item in a:
  			c.append(a)

  	print (c)




if __name__ == "__main__":
	main()
