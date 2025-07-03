
    #Try It YourSelf
#2.1 Simple message
'''Assign message to the variable, and then print the message'''
message = "I am code phantom" #define and assign message variable to I am code phantom value.
print(message) #display the message in consule that assign above.

#2.2 Simple message 
'''Assign message to the variable, and print the message,
 then change first variable value to new message then print new value of the message'''
alert = "Don't do it!" #alert variable assign to value don't do it!
print(alert) #display alert orginal value.
alert = "Do it!" #alert variable value is change from Don't do it! to Do it
print(alert) #now it display new value of variable alert called Do it!

#2.3 Personal Message
'''Use variable to represent a person's name and print a message to that person. Your message 
should be simple, such as, "Hello phantom, would you like to learn same Python today?'''
 
name = "Phantom" #name is defined and assign value to name
print(f"Hello {name}, would you like to learn same Python today?") # print a message using modern formating which f-string which enable us to embedded varible inside string.

#2.4 Name Cases
'''Use a variable to represnt a person's name, and then print that person's name in 
lowercase, uppercase, and title case.'''
person_name = "Linus Torvald"
print(person_name.lower()) #display all character in lowercase.
print(person_name.upper()) #display all character in uppercase.
print(person_name.title()) #display all character in title case.

#2.5 Famous Quote
'''Find a quote from a famous person you admire. Print the quote and the name of its author.
Your output should look something like the following, including the quotations marks.'''
print('Karl Marx once said: "I am nothing, but I must be everything.') #to print quote we have to use double qoute inside single qoute or vice verse.

#2.6 Famous Quote 2
'''Repeat Exerise 2.5, but this this time, represent line famouse person's name using a variable called famous_person. 
Then compose your message and represent it with a new variable called message. 
Print your message.'''
famous_person = "Eleanor Roosevelt"
print(f'{famous_person} once said, The future is belongs to those who believe in the beauty of there dreams.') # use f-string formating and put double quote inside single qoute.

# 2.7 Stripping Names
p_name = "\nKarl Marx\t" #which new line in first the name then whitespace
print(p_name) #display with both tab whitespace anad new line whitespace.
print(p_name.rstrip()) #display only left whitespace and name are displayed, but right sidespace will deleted or ignored.
print(p_name.lstrip()) # display only right whitespace and name are displayed, but left side whitespace will deleted or ignored.
print(p_name.strip()) # display only the name neither right side nor left side white space is not shown.
