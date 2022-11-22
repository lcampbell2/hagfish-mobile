from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

import random

#LIGHT_COLOUR = (255, 0, 0)

#PIXEL_ARRAY = [LIGHT_COLOUR] * 64

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
global LIGHT_COLOUR
LIGHT_COLOUR = [r, g, b]
global RANDOM_COLOUR
RANDOM_COLOUR = [LIGHT_COLOUR] * 64

MORSE_CODE_DICT = {'A':'.-', 'B':'-...',
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
                    '(':'-.--.', ')':'-.--.-', ' ':'*'}

TIMING_DICT = {'.': 0.2, '-': 1.0, ' ': 2.0, '*': 0.0}

# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    message = message.upper()
    cipher = ''
    for letter in message:
        if letter != ' ':
 
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += '*'
            #print(cipher)
 
    return cipher

def make_code_list(message):
    #encrypt the message
    codedmessage = encrypt(message)
    # split message into letters
    list = codedmessage.split(" ")
    #return our list of letters
    return list

# takes in list of encoded letters, outputs flashes of light
def morse_code(message):
    import random
    # get list
    list = make_code_list(message)
    # iterate through letter list
    for letter in list:
        # iterate through each beep
        print("start of letter")
        for beep in letter:
            print (beep)
            # display the lights
            global LIGHT_COLOUR
            sense.set_pixels([LIGHT_COLOUR] * 64)
            # wait for time based on beep
            sleep(TIMING_DICT[beep])
            # turn off lights
            sense.clear()
            sleep(0.2)
            #end of letter
            if beep == '*':
                r = random.randint(0,255)
                g = random.randint(0,255)
                b = random.randint(0,255)
                LIGHT_COLOUR
                LIGHT_COLOUR = [r, g, b]
                global RANDOM_COLOUR
                RANDOM_COLOUR = [LIGHT_COLOUR] * 64
                sleep(3)
                print("new word/colour change")
        
       
        
    #sense.set_pixels(PIXEL_ARRAY)
    #sleep(5)
    #sense.clear()
    
    
    
morse_code("Alex is a creeper")
