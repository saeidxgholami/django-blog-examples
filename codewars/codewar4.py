def alphabet_position2(text):
    text = text.lower()
    alph = []
    text_pos = ""

    for x in range(97, 123):
        alph.append(chr(x))

    
    for char in text:
        if char.isalpha():
            text_pos += str(alph.index(char)+1) + " "

    return text_pos

def alphabet_position(text):
    x = ' '.join(str(ord(ch.lower()) - 96)  for ch in text if ch.isalpha())
    return x



def decrypt(encrypted_text, n):
    pass


def encrypt(text, n):
    if n <= 0:
        return text

    if n == 1:
        return text[1::2] + text[::2] 

    if n > 1:
        c = text[1::2] + text[::2] 
        
        for i in range(n-1):
            c = c[1::2] + c[::2] 

        print(c)

    

encrypt("This is a test!", 4)