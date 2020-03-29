import math

#Function to determine if specified number is a valid prime
def is_prime(number): 
    if number <= 1: #eliminates negative numbers, 0, and 1
        print("Not a prime.")
        return False

    elif number <= 3: #will evaluate 2 and 3 as, correctly, prime
        print("Is a prime.")
        return True

    elif number%2==0 or number%3==0: #will eliminate numbers that are multiples of 2 or 3
        print("Not a prime.") #so we can begin checking 6k +/- 1 algorithm
        return False

    else:
        i = 5
        while i**2 <= number:
            if number%i==0 or number%(i+2)==0:
                print("Not a prime")
                return False
            i += 6
        print("Is a prime.")
        return True

def compute_n(p, q):
	n = p * q
	print(n)
	return n

user_input = input("Choose rsa value to compute: prime n l(n) e d:\n>>".strip().lower())
while user_input != 'q':
	if user_input == 'prime':
		number = int(input("Enter value to be checked:\n>>"))
		is_prime(number)
	elif user_input == 'n':
		p, q = int(input("Enter value for p:\n>>")), int(input("Enter value for q:\n>>"))
		compute_n(p, q)
	elif user_input == 'l(n)':
		pass
	elif user_input == 'e':
		pass
	elif user_input == 'd':
		pass
	user_input = input("Choose rsa value to compute: prime n labmda(n) e d ('q' to quit)".strip().lower())


