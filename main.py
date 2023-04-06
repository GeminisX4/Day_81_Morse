from morse import morse
texto = input("Input text: ")
new_texto = ""

for _ in range(len(texto)):
    new_texto += morse[texto[_].upper()]
    new_texto += "   "

print(new_texto)