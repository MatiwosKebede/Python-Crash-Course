# String_Methods
# String methods are built-in functions that allow you to analysis and manipulate strings in python.
# for example upper(), lower(), title(), striop(), rstrip(), lstrip(), split(), join(), replace(), find(), count() and many other methods. are exist in python.

message = "        Hello, world!-------"
print(message) # Output: "       Hello, world!-------"
# upper() method is used to convert all characters of a string to uppercase.
print(message.upper()) # Output: "      HELLO, WORLD!-------"
# lower() method is used to convert all characters of a string to lowercase.
print(message.lower()) # Output: "       hello, world!-------"
# title() method is used to convert the first character of each word in a string to uppercase and the rest to lowercase.
print(message.title()) # Output: "        Hello, World!-------"
# strip() method is used to remove leading(from the start) an trailing(from the end) whitespace or specified characters from a string.
print(message.strip()) # Output: "Hello, world!-------"
# rstrip() method is used to remove trailing whitespace or specified characters form end of a string.
print(message.strip('-')) # Output: "        Hello, world!"
# lstrip () method is used to remove leading whitepace or specified characters from the start fo a string.
print(message.lstrip()) # Output: "Hello, world!-------"
# split() method is used to separate(split) whhitespace or specified characters from the stirng into a list of substrings.
print(message.split()) # Output: ['Hello,', 'world!--------']
# join() method is an inverse of split() method, it is used to join a list of strings into a single string with a specfied separator.
words = ["hello", "world", "!"]
print(" ".join(words)) # Output: "hello world !"
# replace() method is used to replace a specified substring with another substring in a string.
print("Hello, world!".replace("world", "python")) # Output: "Hello, python!"
# find() method is used to search and find the first occurrence of substring in a stirng and returns its index.
print(message.find("world")) # Output: 15
# count() method is used to count the number of occurrneces of a specified substring in a string.
print(message.count("o")) # Output: 2
# isalpha() method is used to check if all characters in a string are alphabetic (letters only), its returns True or False.
print("Hello world".isalpha()) # Output: False (because of space)
print("Hello".isalpha()) # Ourpur: True (because all characters are letters)
# isdigit() method is used to check if all characters in a string are digits (numbers only), its retruns True or False.
print("884349585".isdigit()) # Output: True (because all characters are digtis)
print("123455a".isdigit()) # Output: False (becasue its contains a letter)
# isalnum() method is used to check if all characters in a string are alphanumeric (letters and digits) and returns True or False.
print("ABcd1234".isalnum()) # Output: True (because all characters are alphanumeric)
print("ABcd 1234".isalnum()) # Output: False (becaus of space)
# startswith() method is used to check if a string start with a specified substring and returns True or False.
print("Python crash course".startswith("Python")) # Output: True
print("Python crash course".startswith("crash"))  # Output: False
# endswith() mehtod is used to check if a stirng ends with a specified substring and returns True or False.
print("Code Phantom".endswith("tom")) # Output: True
print("Code Phantom".endswith("Code")) # Output: False
# format() method is used to format a string by inserting values into placeholders.
name = "Alex"
age = 20
print("my name is {} and I am {} years old.".format(name, age)) # Output: "my name is Alex and I am 20 years old."