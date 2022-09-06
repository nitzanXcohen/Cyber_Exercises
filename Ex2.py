CODE = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---',
'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-',
'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....',
'7':'--...', '8':'---..', '9':'----.','0':'-----', ', ':'--..--', '.':'.-.-.-',
'?':'..--..', ' / ':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-', ' ':'/'}
def decrypt(message):
    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(CODE.keys())[list(CODE.values()).index(citext)]
                citext = ''
    return decipher

def check_freq(str):
    freq = {}
    for char in set(str):
        freq[char] = str.count(char)
    return freq

def main():
    list = []
    message = open("morse2.txt").read()
    try:
        print(decrypt(message))
       # for char in decrypt(message):
        #   print(char , " = " ,decrypt(message).count(char))
        print(check_freq(decrypt(message)))

    except ValueError:
        print("Error in Morse Code")
if __name__ == '__main__':
    main()
