alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  for letter in start_text:
    if letter == " ":
      end_text += " "
    else:
      position = alphabet.index(letter)
      if cipher_direction == "encode":
        new_position = position + shift_amount
        if new_position > 25:
          new_position = new_position - 26
          end_text += alphabet[new_position]
        else:
          end_text += alphabet[new_position]
  
      elif cipher_direction == "decode":
        new_position = position - shift_amount
        if new_position < 0:
          new_position = 26 + new_position
          end_text += alphabet[new_position]
        else:
          end_text += alphabet[new_position]
        
  print(f"The {cipher_direction}d text is {end_text}")