import random
import math
import Crypto.Util.number

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
	
def generate_keys(p, q, e=0):
	if not is_prime(p):
		print("{} is not prime. Values 'p' and 'q' must be prime.".format(p))
		return False
	if not is_prime(q):
		print("{} is not prime. Values 'p' and 'q' must be prime.".format(q))
		return False
	n = compute_n(p, q)
	ln = carmichael_totient(p, q)
	if e == 0:
		e = compute_e(p, q)
	else:
		if verify_e(e, p, q):
			pass
		else:
			print("{} not a valid value for 'e'. Must be coprime with lambda(n) and between 1 and lambda(n).".format(e))
	d = compute_modular_inverse(e, ln)
	public_key, private_key = (n, e), (n, d)

	print("\nPublic key:", public_key, "\nPrivate key:", private_key, "\n")
	return public_key, private_key

message = 6357294171489311547190987615544575133581967886499484091352661406414044440475205342882841236357665973431462491355089413710392273380203038793241564304774271529108729717
e = 3
n = 29129463609326322559521123136222078780585451208149138547799121083622333250646678767769126248182207478527881025116332742616201890576280859777513414460842754045651093593251726785499360828237897586278068419875517543013545369871704159718105354690802726645710699029936754265654381929650494383622583174075805797766685192325859982797796060391271817578087472948205626257717479858369754502615173773514087437504532994142632207906501079835037052797306690891600559321673928943158514646572885986881016569647357891598545880304236145548059520898133142087545369179876065657214225826997676844000054327141666320553082128424707948750331
c = pow(message, e, n)
print(c)

p = 153143042272527868798412612417204434156935146874282990942386694020462861918068684561281763577034706600608387699148071015194725533394126069826857182428660427818277378724977554365910231524827258160904493774748749088477328204812171935987088715261127321911849092207070653272176072509933245978935455542420691737433
n = 23952937352643527451379227516428377705004894508566304313177880191662177061878993798938496818120987817049538365206671401938265663712351239785237507341311858383628932183083145614696585411921662992078376103990806989257289472590902167457302888198293135333083734504191910953238278860923153746261500759411620299864395158783509535039259714359526738924736952759753503357614939203434092075676169179112452620687731670534906069845965633455748606649062394293289967059348143206600765820021392608270528856238306849191113241355842396325210132358046616312901337987464473799040762271876389031455051640937681745409057246190498795697239
q = int(n//p)
e = 65537
c = 9276182891752530901219927412073143671948875482138883542938401204867776171605127572134036444953137790745003888189443976475578120144429490705784649507786686788217321344885844827647654512949354661973611664872783393501992112464825441330961457628758224011658785082995945612195073191601952238361315820373373606643521463466376095236371778984942891123936191796720097900593599447528583257806196551724676380135110693228330934418147759387990754368525068685861547977993085149359162754890674487823080750579601100854795031284533864826255207300350679553486505961837349042778851010569582458629638648589442067576234798724906377157351
totient = (p-1)*(q-1)
d = compute_modular_inverse(e, totient)
p = pow(c, d, n)
print(p)
