#Cryptography can be easy, do you know what ROT13 is?


message = input()
def rot13(text):
    result = ''
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encoded_char = chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset)
            result += encoded_char
        else:
            result += char
    return result
flag = rot13(message)

print(flag)
