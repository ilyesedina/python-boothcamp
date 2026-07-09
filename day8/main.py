# Encode and decode messages
from caesar_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs and returns the encrypted text.
# TODO-2: Call the encrypt function and pass the user inputs. Print the encrypted text.
# TODO-3: Create a function called 'decrypt' that takes the 'text' and 'shift' as inputs and returns the decrypted text.
# TODO-4: Call the decrypt function and pass the user inputs. Print the decrypted text.


def caesar(start_text, shift_amount, encode_or_decode):
    output_text = ""

    shift = shift_amount
    if encode_or_decode == "decode":
        shift *= -1

    for letter in start_text:

        if letter not in alphabet:
            output_text += letter
        else:

            shifted_position = alphabet.index(letter) + shift
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here's the {encode_or_decode}d result: {output_text}")

should_continue = True
while should_continue:
    description = input("Type 'encode' to encrypt, type 'decode' to decrypt i made some changes :)))))))):\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, encode_or_decode=description)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")


