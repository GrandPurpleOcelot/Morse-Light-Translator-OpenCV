MORSE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', ' ':'_'} # special case: space is represented by '_' in morse

MORSE_DICT_REVERSED = {value:key for key,value in MORSE_DICT.items()}

def convertMorseToText(morse_string):

    # avoid error if no light pulse detected yet
    while True:
        try:
            message = ''.join([MORSE_DICT_REVERSED.get(i, '*') for i in morse_string.split(' ')]) # special case '*' means no letter found
            return message
            break
        except (TypeError, AttributeError):
            return "No message detected"



