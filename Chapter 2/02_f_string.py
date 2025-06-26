#formating strings using older style.
print("my name is %s and I am %i years old." % ("Alex", 20)) # Output: "my name is Alex and I am 20 years old."
print("my name is {} and I am {} years old.".format("Alex", 20)) # Output: "my name is Alex and I am 20 years old."

# f-strings (formatted string literals) are a modern way to format strings in python, they allow embed expressions inside strings using curly braces {} and character f or F before the string."
name = "Alex"
age = 20
print(f"my name is {name} and I am {age} years old.") # Output: "my name is Alex and I am 20 years old."
"