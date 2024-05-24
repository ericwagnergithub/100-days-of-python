import caesar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(caesar_art.logo)

def caesar(plain_text, shift_amount, cipher_direction):
    cipher_text =""
    
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


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 #Accounts for shift larger than 26

    caesar(text, shift, direction)
    if input("Type 'yes' if you want to go again. Otherwise type 'no'.\n ").lower() == 'no':
        should_continue = False
        print("Goodbye.")