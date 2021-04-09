import art

def caesar_cipher(text, shift, direction):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    max_index = len(alphabet)-1
    result = ""

    for i in range(len(text)):
        try:
            index = alphabet.index(text[i])
        except ValueError:
            index = i
        
        if direction == 'encode':
            new_index = index+shift
        else:
            new_index = index-shift
        
        if text[i] not in alphabet:
            result += text[i]
        elif new_index > max_index or new_index < 0:
            new_index = new_index % max_index
            result += alphabet[new_index]
        else:
            result += alphabet[new_index]
    
    print(f"The {direction}d text is {result}")

print(art.logo)

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(text, shift, direction)
    
    should_continue = input("Type 'y' if you want to cipher a message again: ").lower()

    if try_again == 'y':
        should_continue = False