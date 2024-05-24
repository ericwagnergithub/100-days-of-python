import caesar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(caesar_art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(plain_text, shift_amount, cipher_direction):
    cipher_text =""
    shift_amount = shift_amount % 26
    for letter in plain_text:
        if letter in alphabet:
            alpha_num = alphabet.index(letter)
            if cipher_direction == "encode":
                new_letter = alphabet[alpha_num + shift_amount]
            elif cipher_direction == "decode":
                new_letter = alphabet[alpha_num - shift_amount]
        else:
            new_letter = letter    
        cipher_text += new_letter
    print(f"The {cipher_direction}d text is {cipher_text}.")


# def encrypt(plain_text, shift_amount):
#     cipher_text =""
#     for letter in plain_text:
#         alpha_num = alphabet.index(letter)
#         if shift_amount + alpha_num > 26:
#             alpha_num -= 26
#         new_letter = alphabet[alpha_num + shift_amount]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}.")

# def decrypt(plain_text, shift_amount):
#     cipher_text =""
#     for letter in plain_text:
#         alpha_num = alphabet.index(letter)
#         if alpha_num - shift_amount < 0:
#             alpha_num += 26
#         new_letter = alphabet[alpha_num - shift_amount]
#         cipher_text += new_letter
#     print(f"The decoded text is {cipher_text}.")

# if cipher_direction.lower() == "encode":
#     encrypt(text, shift)
# elif cipher_direction.lower() == "decode":
#     decrypt(text, shift)

caesar(text, shift, direction)