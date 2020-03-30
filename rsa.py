import random
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
            '''would like to try number%(i-1)==0 and number%(i+1)==0 to more 
			closely mirror the actual pattern; may be slower since 'i' is 
			modified 2x rather than once
			'''
            if number%i==0 or number%(i+2)==0: 
                print("Not a prime")
                return False
            i += 6
        print("Is a prime.")
        return True

def compute_n(p, q):
	n = p * q
	return int(n)

def compute_lambda_n(p, q):
	return int(compute_lcm(p-1, q-1))

def compute_gcd(a, b):
	if a == 0:		#if the value of a is 0, then b is the gcd
		return b 
	elif b == 0:	#likewise, if the value of b = 0, then a is the gcd
		return a 
	else:
		a, b = b, a%b #if neither is zero, we run gcd on a new value for a and b
		return int(compute_gcd(a, b)) #recursively, returning the recursive result

def compute_lcm(a, b):
	lcm = (a * b)/compute_gcd(a, b)
	return int(lcm)

def compute_e(p, q, e=0):
	n = p * q
	if e == 0:
		e = random.randint(2, n)

	if 1<e<n:
		
	elif user_e == "":
		e = random.randint(2,n)
		coprime = gcd(e, compute_lambda_n(

'''
user_input = input("Choose rsa value to compute: prime n l(n) e d:\n>>".strip().lower())
while user_input != 'q':
	if user_input == 'prime':
		number = int(input("Enter value to be checked:\n>>"))
		is_prime(number)
	elif user_input == 'n':
		p, q = int(input("Enter value for p:\n>>")), int(input("Enter value for q:\n>>"))
		compute_n(p, q)
	elif user_input == 'l(n)':
		p, q = int(input("Enter value for p:\n>>")), int(input("Enter value for q:\n>>"))
		compute_lambda_n(p, q)
	elif user_input == 'gcd':
		a = int(input("a: "))
		b = int(input("b: "))
		compute_gcd(a, b)
	elif user_input == 'lcm':
		a = int(input("a: "))
		b = int(input("b: "))
		compute_lcm(a, b)
	elif user_input == 'e':
		print("Would you like to enter a value for 'n' or use the stored value?")
		user_input = input(
		user_e = int(input("Enter value for 'e' or 0 for random value:\n>>".strip().lower()))
		compute_e(n, user_e)
	elif user_input == 'd':
		pass
	user_input = input("Choose rsa value to compute: prime n labmda(n) e d ('q' to quit)".strip().lower())
'''
