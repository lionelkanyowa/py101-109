# Print a new version of the sequence given by `advice` that ends just before the word `house`.
# Don't worry about spaces or punctuation: remove everything from the beginning of `house` to the
# end of the sentence.
# 

advice = "Few things in life are important as house training your pet dinosaur."  
print(advice.split("house")[0])

# Output:  Few things in life are important as 