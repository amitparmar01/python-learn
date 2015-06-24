
import random 

def common_list(a, b):
    #a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 2, 1, 3, 4, 00]
    #b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    common = []
    big = []
    small = []

    if len(a) > len(b):
        big  = a
        small = b
    else:
        big = b
        small = a

    for item in big:
        if item in small and not item in common:
            common.append(item)

    return sorted(common)

def main():

    lengthA = random.randint(1, 20)
    lengthB = random.randint(1, 20)

    a = random.sample(range(1, 101), lengthA)
    b = random.sample(range(1, 101), lengthB)

    print(common_list(a,b))

if __name__ == "__main__":
	main()
