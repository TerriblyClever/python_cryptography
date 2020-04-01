import random
import math

#Function to determine if specified number is a valid prime
def is_prime(number): 
    if number <= 1: #eliminates negative numbers, 0, and 1
        return False

    elif number <= 3: #will evaluate 2 and 3 as, correctly, prime
        return True

    elif number%2==0 or number%3==0: #will eliminate numbers that are multiples of 2 or 3
        return False #so we can begin checking 6k +/- 1 algorithm

    else:
        i = 5
        while i**2 <= number:
            '''would like to try number%(i-1)==0 and number%(i+1)==0 to more 
			closely mirror the actual pattern; may be slower since 'i' is 
			modified 2x rather than once
			'''
            if number%i==0 or number%(i+2)==0: 
                return False
            i += 6
        return True

def compute_n(p, q):
	n = p * q
	return int(n)

def carmichael_totient(p, q):
	return int(compute_lcm(p-1, q-1))

#strictly speaking, this function not necessary for the RSA encryption file
#it was written for a specific picoCTF problem, rsa-pop-quiz
def euler_totient(n):
	'''
	#solution making use of brute-force method fore Euler totient function
	phi = 1
	for number in range(2, n):
		if compute_gcd(number, n)==1:
			phi += 1
	'''
	#solution making use of Euler product function
	phi = n
	p = 2
	while p**2 < n:
		if n%p == 0: #checks if p is a prime factor
			while n%p == 0:
				n = n // p
			phi = phi * (1.0 - (1.0 / float(p))) #update the number of coprimes based on product function
		p += 1 #could this be modified to follow the primes pattern 6k +/- 1?
	
	if n > 1:
		phi = phi * (1 - 1/float(n))
	return int(phi)

def compute_gcd(a, b):
	if a == 0:		#if the value of a is 0, then b is the gcd
		return b 
	elif b == 0:	#likewise, if the value of b = 0, then a is the gcd
		return a 
	else:
		a, b = b, a%b #if neither is zero, we run gcd on a new value for a and b
		return int(compute_gcd(a, b)) #recursively, returning the recursive result

#function used to calculate the modular inverse of 'e', i.e. 'd' for RSA encryption
def compute_modular_inverse(e, ln):
	m0 = ln 
	y = 0
	x = 1

	if ln == 1:
		return 0

	while e > 1:
		#q is quotient
		q = e//ln
		t = ln

		#lambda_n will now be the remainder and this will process like Euclid's algorithm
		ln = e%ln
		e = t
		t = y

		#update x and y
		y = x - (q * y)
		x = t
	if x < 0:
		x = x + m0

	return x

def compute_lcm(a, b):
	lcm = (a * b)/compute_gcd(a, b)
	return int(lcm)

def compute_e(p, q):
	e = 0
	n = p * q
	carmichael = carmichael_totient(p, q)
	while compute_gcd(e, carmichael) != 1:
		e = random.randint(2, n)
		#FUNCTION UNFINISHED; need to add functionality to increase security,
		#measure bit-length/Hamming weight for encryption efficiency
	return e	

def verify_e(e, p, q):
	n = p * q
	carmichael = carmichael_totient(p, q)
	if 1<e<n and compute_gcd(e, carmichael) == 1:
		return True 
	else:
		return False	
	

