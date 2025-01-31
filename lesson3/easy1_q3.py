# 3. STarting with the string:

famous_words = "seven years ago..."

# Show two different ways to create a new string "Four score and" prepend to the front of the string
# referenced by famous_words

prepend_word = "Four score and"

print(f'{prepend_word} {famous_words} ' )
print(prepend_word + ' ' + famous_words )
print("Four score and " + famous_words)
print(f"Four score and {famous_words}")