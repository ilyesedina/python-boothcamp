# Encode and decode messages

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

description = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs and returns the encrypted text.
# TODO-2: Call the encrypt function and pass the user inputs. Print the encrypted text.
# TODO-3: Create a function called 'decrypt' that takes the 'text' and 'shift' as inputs and returns the decrypted text.
# TODO-4: Call the decrypt function and pass the user inputs. Print the decrypted text.
#Hello 2
def encrypt(original_text, shift_amount):
    cipher_text = ""

    for latter in original_text:
        shifted_position = alphabet.index(latter) + shift_amount # 7 -> 9
        shifted_position %= len(alphabet) # we are always in the range of 0-25
        cipher_text += alphabet[shifted_position] # H -> J

    print(f"Here is the encoded result {cipher_text}")

encrypt(original_text=text, shift_amount=shift)

def decrypt(cipher_text, shift_amount):
    original_text = ""

    for latter in cipher_text:
        shifted_position = alphabet.index(latter) - shift_amount # 9 -> 7
        shifted_position %= len(alphabet) # we are always in the range of 0-25
        original_text += alphabet[shifted_position] # J -> H

    print(f"Here is the decoded result {original_text}")

decrypt(cipher_text=text, shift_amount=shift)

