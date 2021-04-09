

def caesar_cipher(text, shift, direction):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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
        elif new_index > 25  or new_index < 0:
            new_index = new_index % 25
            result += alphabet[new_index]
        else:
            result += alphabet[new_index]
    
    if direction == 'encode':
        print(f"The encoded text is {result}")
    else:
        print(f"The decoded text is {result}")

# def encrypt(text, shift):
#     alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     result = ""
  
#     for i in range(len(text)):
#         try:
#             index = alphabet.index(text[i])
#         except ValueError:
#             index = i
        
#         if text[i] not in alphabet:
#             result += text[i]
#         elif index+shift > 25:
#             index = (index+shift) % 25
#             result += alphabet[index]
#         else:
#             result += alphabet[index+shift]
    
#     print(f"The encoded text is {result}")

# def decrypt(text, shift):
#     result = ""
  
#     for i in range(len(text)):
#         try:
#             index = alphabet.index(text[i])
#         except ValueError:
#             index = i
    
#         if text[i] not in alphabet:
#             result += text[i]
#         elif index-shift < 0:
#             index = (index-shift) % 25
#             result += alphabet[index]
#         else:
#             result += alphabet[index-shift]
    
#     print(f"The decoded text is {result}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar_cipher(text, shift, direction)