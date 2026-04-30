# Create name check code


# get input
input_test = input("Enter names of people met in the last 24 hours: ")

# convert input to lowercase for case-insensitive comparison
input_test = input_test.lower()

# check for "John"
print("John in input =", "john" in input_test)

# check for your name (hard coded)
print("Moussa in input =", "moussa" in input_test)

# challenge – two more names
print("Mary in input =", "mary" in input_test)
print("David in input =", "david" in input_test)
