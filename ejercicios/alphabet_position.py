def alphabet_position(text:str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    position = ""

    for index, character in enumerate(text):
        validation = character in alphabet
        
        if validation == True:
            index = alphabet.index(character)
            index = index + 1 
            position = position + str(index) + " "

    position = position.strip()
    return position