# 11. Write a function that determines and returns the UTF-16 string value of a string passed in as an argument. The UTF-16 
# string value is the sum of the UTF-16 values of every character in the string. (You may use `ord` to determine the UTF-16 
# value of a character.)

def utf16_value(word):
    word_sum = 0
    for char in word:
        word_sum += ord(char)
    return word_sum

# These should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

