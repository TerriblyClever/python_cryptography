import string

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ' #letters in English listed by frequency
LETTERS = string.ascii_uppercase
letter_count = {}

for letter in LETTERS:
	letter_count[letter] = 0

def get_letter_count(message):
	for letter in message:
		if letter in LETTERS:
			letter_count[letter] += 1

