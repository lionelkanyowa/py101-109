# In the previous problem, our first answer added 'Dino' to the list like this:

flinstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flinstones.append("Dino")

# How can we add multiple items to our list(e.g., 'Dino' and 'Hoppy')? Replace the call to `append`
# with another method invocation.

flinstones.extend(["Dino", "Hoppy"])

print(flinstones)
