# The following function unnecessarily uses two return statements to return boolean values. 
# Can you rewrite this function so it only has one return statement and does not explicitly 
# use either True or False?

def is_color_valid(color):
    # return(if color == "blue" or color == "green" else)
    # return color == "blue" or color == "green"
    return color in ["blue", "green"]
    # if color == "blue" or color == "green":
        # return True
    # else:
        # return False
    
