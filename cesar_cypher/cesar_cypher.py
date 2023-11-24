lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

max_lowercase = ord('z')
max_uppercase = ord('Z')

encoded_str = ""
for char in secret:
    
    if char.isalpha():
        
        encode = ord(char) + cipher

        if char.isupper() and encode > max_uppercase:
            diff = encode - max_uppercase
            encode = ord('A') + diff - 1
        elif char.islower() and encode > max_lowercase:
            diff = encode - max_lowercase
            encode = ord('a') + diff - 1
        
        encoded_str += chr(encode)

    else:
        encoded_str += char

print(encoded_str)