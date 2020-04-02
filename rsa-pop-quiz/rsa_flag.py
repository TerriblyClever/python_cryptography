plaintext = 14311663942709674867122208214901970650496788151239520971623411712977119642137567031494784893

hex_plaintext = (hex(plaintext)[2:])
print(str(hex_plaintext))

bytes_object = bytes.fromhex(hex_plaintext)
print(bytes_object)

ascii_plaintext = bytes_object.decode("ASCII")
print(ascii_plaintext)
