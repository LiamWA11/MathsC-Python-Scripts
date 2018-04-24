x = input("text: ").lower()                             # Input for the text to encode
shift = int(input("shift: "))                           # Input for the shift to encode text with
split = int(input("split: "))                           # Input for the split of the outputted text

x = x.replace(" ", "")                                  # Gets rid of teh spaces in the input text

out = ""                                                # Variable declaration: output text variable
a, b = 0, 0                                             # Variable declaration: placeholder variables

for char in x:                                          # For every character in variable x (input text)
    foo = ord(char)-97                                  # Set variable foo equal to the ascii value of that
                                                        #  character to 97, so that the value for character A is 0
    baa = chr((foo+shift) % 26 + 97)                    # Set variable baa to the character of the ASCII code, after
                                                        #  it has been shifted by the specificed amount, mod 26 and
                                                        #  then reset to original ASCII value range by adding 97 to it
    out += baa                                          # Add the encoded character to the output variable


while a < x.__len__():
    if b < split-1:
        print(out[a], end="")
        b += 1
    elif b == split-1:
        print(out[a], end=" ")
        b = 0
    a += 1
if x.__len__() % split != 0:
    print(out[a-1]*(split-(x.__len__() % split)))

print("")
