# Create a function that takes 2 arguments, a list and a dictionary. This list will contain 2 or more
# elements that, when joined with spaces, will produce a person's name. The dictionary will contain
# two keys, "title" and "occupation", and the appropriate values. your function should return
# a greeting that uses the person's full name, and mentions the person's title.

def greetings(name, status):
    return(f"Hello, {' '.join(name)}! Nice to have a "
           f"{status.get('title')} {status.get('occupation')} "
           "around.")

greeting = greetings(
    ["john", "Q", "Doe"],
    {"title": "Master", "occupation": "Plummer"}

)

print(greeting)