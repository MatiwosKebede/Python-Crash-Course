
# 📘 Python Crash Course – Chapter 2: Variables and Simple Data Types

In the previous chapter, we created our first Python file hello_world.py and ran our first line of code:

<pre >   hello_world.py  
   print("Hello World")
</pre>
Output:

Hello World

## 🎯 Chapter 2 Overview

#### In this chapter, we explore:

   #### Variables and how to use them

   #### Simple data types: string, integer, float, and boolean

   #### Formatting and combining strings

   #### Common string methods

   #### Comments and constants

#### 🧠 What is a Variable?

### A variable is a named container used to store data in programming.
### ✅ Why are variables important?

   #### They help store, organize, and reuse data.

   #### They are essential in all real-world programs.

#### 📌 Python Variable Naming Rules

   #### Use only letters, numbers, and underscores (_).

   #### *Variable names must not begin with a number (e.g., 1var ❌, _1var ✅).*

   #### Do not use Python reserved words like print, def, etc.

   #### Spaces are not allowed (e.g., hello world ❌, hello_world ✅).

   #### Use short, descriptive names (e.g., age = 20 is better than x = 20).

### 🛠️ Python is case-sensitive:

myVar = 10
MyVar = 20
print(myVar)  # 10
print(MyVar)  # 20

### ✏️ Example 1: Storing Age

age = 10
print(age)

Output:

10

💪 Exercise:

## Create a variable called Customer_Name that stores a customer’s name and display it.
🔢 Simple Data Types in Python

### Python has 4 main simple data types (each holds a single value):
Type	Keyword	Description
String	str	A series of characters
Integer	int	Whole numbers
Float	float	Decimal numbers
Boolean	bool	True or False values
## 1️⃣ String

A string is any text in quotes:

message1 = "I am a Python string"
message2 = 'I am also a Python string'
name = "phantom code"
### string methods
those are upper(), lower(), title(), count(), find(), startswith(), endswith(), isdigit(), isalpha(), isalnum(), and other.
upper() is a method used to convert all characters in string to uppercase.
e.g *print("python crash course".upper())*
Output: *PYTHON CRASH COURSE*
lower() is a method used to convert all characters into lowercase.
e.g *print("Hello Phantom")
Output: *hello phantom*
title() is a method used to convert all characters of each starting character upper case and the rest all characters to lowercase.
e.g *print("hello world".title())*
    *Hello World"
count() is a method used to count specified substring or all string characters numbers.
e.g "print("python crash course.count("o"))*
Output: *2*
find() is a method used to search find substring and return its first occurred searched substring.
e.g *print("python crash course".find("course"))
Output: *python crash course*
startswith() is a method used to search then return if its find specified substring in string.
e.g *print("python crash course".startswith("python"))*
Output: *True*
endswith() is a method used to search find substring that found at the end its return True or False.
e.g *print("python crash course".endswith("course))*
Output: *True*
isalpha() is a method used to check alphabet its return true if all character are alphabet other ways i return false.
e.g *print("python crash course".isalpha()) # this will display False because of the space.*
    *print("Phantom".isalpha())*
Output: *False*
Output: *True*
isdigit() is a method used to check whether all string characters are digits its return true or false.
e.g *print("12345".isdigit())*
Output: *True*
isalnum() is a method used to check all string characters are consists of number and alphabet only its return if exist and false if not"
*print("password1234".isalnum()) *
Output: *True*

### String Variables in Strings (f-strings)
f-strings is a modern formating python code which is introduced after python 3.6, its is embed expression inside string curly brace {} and f or F.
e.g
*country  = "Barbados"
city = "Bridgetown"
location = f"{country}, {city}*
print(location)*
Output: *BarBados, Bridgetown*
e.g
*name = "Alex"
print(f"Hello, {name}.")*
Output: *Hello, Alex.*

strings can include quotes:

quote = "I'm learning Python"
quote2 = 'He said "Python is great!"'

### 🔣 Escape Characters
Code	Meaning
\n	New line
\t	Tab space

print("\nPython Crash Course.")
print("\tPython Crash Course.")
print("\n\tPython Crash Course.")

⚠️ Common String Error

❌ This will cause an error 
myVar = 'I'm fine'

✅ Correct way 
myVar = "I'm fine"
country = "Barbados"

🧹 Stripping Whitespace

* text = "   this is text   "
print(text.strip())    # both sides
print(text.lstrip())   # left only
print(text.rstrip())   # right only

course = "------python crash course---------"
print(course.lstrip("-"))
print(course.rstrip("-"))
print(course.strip("-")) *

# 2️⃣ Numbers – Integers and Floats
e.g 
* age = 25
print(f"My age is: {age}")
*
Output: *My age is: 25 *
e.g 
*num1 = 5
num2 = 7
sum = num1 + num2
print(sum)  # 12
*
Output: *12*

⚠️ Operation Result Types
Operation	Result Type
float + int	float
int + float	float
int + int	int
💡 Large Numbers for Readability

num = 1_000_000
print(num)  # 1000000

## 3️⃣ Boolean (True / False)

is_active = True
is_banned = False
print(is_active)
print(is_banned)

📌 Constants

A constant is a variable that should never change.  commonly constants are written in UPPERCASE.

PI = 3.14159
MAX_USERS = 1000

💬 Comments in Python
Single-line comment:

* # This is a comment*

 Multi-line comment: 
*
'''
This is a 
multi-line comment
'''
*
🧘 Bonus: The Zen of Python

Run this in your terminal or script:

import this

You’ll see:

    “Beautiful is better than ugly.
    Explicit is better than implicit...”

This shows the guiding philosophy behind writing clean, readable Python code.
