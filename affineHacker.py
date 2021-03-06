# Affine Cipher Hacker
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import affineCipher, detectEnglish, cryptomath

SILENT_MODE = False

def hackAffine(message):
    print('Hacking...')

    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on Mac and Linux)
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    # Brute-force by looping through every possible key
    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue

        decryptedText = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print('Tried Key %s... (%s)' % (key, decryptedText[:40]))

        if detectEnglish.isEnglish(decryptedText):
            # Check with the user if the decrypted key has been found.
            print()
            print('Possible encryption hack:')
            print('Key: %s' % (key))
            print('Decrypted message: ' + decryptedText[:200])
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None
