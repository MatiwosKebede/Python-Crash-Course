# TRY IT YOURSELF

#exerise 3.1 Names
'''Store the names of a few of your friends in alist called names.
Print each person's by accessing each element in the ist, one at a time.'''
names = ["Alex", "Micheal", "James", "Abel"] #Defining and assigning list.
print(names[0]) #Output Alex
print(names[1]) #Output Micheal
print(names[2]) #Output James
print(names[3]) #Output Abel

# exericse 3.2 Greating 
'''Start with the list you used in Exercise 3.1, but instead of just printing each person's name, print a message to them.
The text of each message should be the samae , but each message should be personalized with the person's name'''
print(f"Hi {names[0]}, How was your day!")
print(f"Hi {names[1]}, How was your day?")
print(f"Hi {names[2]}, How was your day?")
print(f"Hi {names[3]}, How was the your day")

# exercise 3.3 Your Own List
'''Think of your favorite mdoe of transportation, such as a motorcycle or a car, and make a list that stores several examples/
Use your list to print a series of statements about these items, such as "I would like to own a Honda motorcycle.'''
cars = ["Tesla", "BYD", "Toyota", "Lamborghini", "Ferarri"]
message = ["I would like to own a ", "I would like to own an "]
print(message[0] + cars[0])

# exercise 3.4 Guest list
'''If you could invite anyone, living or deceased, to dinner, who would you invite?
Make a list that includes at least three people you'd like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.'''
import datetime
invite_names = ["Donald Trump", "Vladimir Putin", "Xi Jinping", "Benjamin Netanyahu", "Emmanuel Macron", "Abiy Ahmed"]
date = datetime.datetime.now()
date_str = str(date)
invitation_message =f"I'm inviting to \nmy Birthday Party which is Jun 29 2025\nI am sure as I will meet you that day."
print(f"{date_str.rjust(50)} \nHello Mr {invite_names[0]} {invitation_message}")
print(f"{date_str.rjust(50)} \nHello Mr {invite_names[1]} {invitation_message}")
print(f"{date_str.rjust(50)} \nHello Mr {invite_names[2]} {invitation_message}")

# exercise 3.5 'changing Guest list
'''You just heard that one of your guests can't make the dinner, so you need to send out a new set of inviations .
You'll have to think of someone else to invite'''
print(f"the name of guest who can't came to party.\n {invite_names[1]}\n {invite_names[0]} \n")