# Convert Text string to Morse Code

user_input = input("Enter the message: ")
morse_dict = {
    # Letters
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    # Digits
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

    # Punctuation
    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'  # Space between words
}

user_input = user_input.upper()

output = ""
for char in user_input:
    if char in morse_dict:
        output += morse_dict[char] + " "  # Add space between Morse symbols
    else:
        output += "[?] "  # Optional: show unknown character as [?]

print("Morse Code Output:\n", output.strip())