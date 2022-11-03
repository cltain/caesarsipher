from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(word, shift_amount, input_dir):
  end_text = ""
  if input_dir == "decode":
    shift_amount *= -1  
  for char in word: 
    if char in alphabet:
      position = alphabet.index(char) 
      new = position + (shift_amount)
      new_letter = alphabet[new]
      end_text += new_letter
    else:
      end_text += char
  print(f"The {input_dir}d text is {end_text}")

print(logo)
cont = True
while cont:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caeser(word = text, shift_amount = shift, input_dir = direction)
  answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if answer == "no":
    cont = False
    print("Goodbye")
