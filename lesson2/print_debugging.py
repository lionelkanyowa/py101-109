def titlize(sentence):
	words = sentence.split() # 2. Check if this is doing the right thing
	# 2. print(words) # added print for debugging
	new_words = []
	
# 3. Check if the loop is properly iterating over all the words in the sentence
	for word in words: 
		# 3. print(word) # testing to see if the loop is working
		if len(word) > 2: # 4. Check the `if` statement
			# 4. print(word)
			word = word.capitalize() # 6. Since strings are immutable, we need to reassign
			# word to the return value.
			# print(word) # 5
		new_words.append(word) # 7. Removed this form the `if` block since we need all words to be printed.
		# print(new_words)

	return ' '.join(new_words)

title = 'hello world of programming'
# 1. print(titlize(title)) 
print(titlize(title))
# titlize(title)
