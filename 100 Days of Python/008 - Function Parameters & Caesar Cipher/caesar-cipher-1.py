alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
text = "zulu"
shift = 5


# shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text_input, shift_input):
    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift
    #  amount and print the encrypted text. e.g. plain_text = "hello" shift = 5 cipher_text = "mjqqt" print output:
    #  "The encoded text is mjqqt"
    encrypted_text = ""
    for letter in text_input:
        shifted_alpha = (alphabet.index(letter) + shift_input)
        encrypted_text += alphabet[shifted_alpha]
    print(f"The encoded text is: {encrypted_text}")


# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
encrypt(text_input=text, shift_input=shift)
