import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(user_message, shift_number, user_choice):
    message = ""
    if direction == "decode":
        shift_number *= -1
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_number
            new_letter = alphabet[new_position]
            message += new_letter
        else:
            message += letter
    print(f"Your message is: {message}")


end_game = False
while not end_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26
    ceaser(user_message=text, shift_number=shift, user_choice=direction)
    restart = input("Type 'yes' to restart the game. Otherwise type 'no'.\n")
    if restart == "no":
        end_game = True
        print("Goodbye")
