alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cesar (plane_text,shift_ammount,type):
  cyfer_text =""
  if type =="encode":
    for letter in plane_text:
      pos=alphabet.index(letter)
      new_pos=pos+shift_ammount
      new_letter=alphabet[new_pos]
      cyfer_text+=new_letter
    print(cyfer_text)
  elif type =="decode":
    for letter in plane_text:
     pos=alphabet.index(letter)
     new_pos=pos-shift_ammount
     new_letter=alphabet[new_pos]
     cyfer_text+=new_letter
    print(cyfer_text)
con=True
while con:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  cesar(plane_text=text, shift_ammount=shift, type=direction)
  res=input("press y to restart or press n to close \n") 
  if res=="n":
    con=False
    
  


  
  
  


  