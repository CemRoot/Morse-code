# Mors Alphabet to Text Converter
# Created by Sam_Lorem @Github Cem_Root @Github
# 2022-10-22

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
        }

CODE_REVERSED = {value: key for key, value in CODE.items()}


def to_morse(s):
    return ' '.join(CODE.get(i.upper()) for i in s)


def from_morse(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split())


Translate = input("Do you want to translate from morse code to text or text to morse code? (morse/text): ")
if Translate == "morse":

    Morse = input("Enter your text: ")
    print(to_morse(Morse))

elif Translate == "text":

    Text = input("Enter your morse code: ")
    print(from_morse(Text))
