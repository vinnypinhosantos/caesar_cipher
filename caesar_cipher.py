from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(start_text, shift_amount, cipher_direction):
  new_text = ""
  for letter in start_text:
    if letter not in alphabet:
      new_text += letter
    else:
      position = alphabet.index(letter)
      if cipher_direction == "encode":
        new_position = position + shift_amount
      elif cipher_direction == "decode":
        new_position = position - shift_amount
      new_text += alphabet[new_position]
  print(f"The {cipher_direction}d message is {new_text}")

print(logo)

def check_direction(cipher_direction):
  while cipher_direction != "decode" and cipher_direction != "encode":
    cipher_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

choice = ""

while choice != "no":  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  check_direction(direction)
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if shift > 26:
    shift %= 26

  cipher(text, shift, direction)

  choice = input("Do you want to restar Caesar Cipher? Yes/No ").lower()
  while choice != "yes" and choice != "no":
    print("You have to print a valid choice")
    choice = input("Do you want to restart Caesar Cipher? Yes/No ").lower()
print("Goodbye!")