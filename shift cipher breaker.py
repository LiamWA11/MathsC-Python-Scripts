cipher = (input("Cipher to crack: ")).replace(" ", "").lower()

for x in range(26):
    for char in cipher:
        foo = ord(char) - 97
        baa = (foo - x - 1) % 26
        baz = chr(baa + 97)
        print(baz, end="")
    print("  -  " + str(x + 1))



