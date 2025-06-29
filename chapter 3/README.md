# Chapter 3
# Introduction to list 
## What is list?
**List** in python is a set of multiple item that store in one variable that can be store and accessed the whole, partially or individually,List can be a collection of any data type and a set from few to millions even greater.
e.g 
<pre>List = ["I am string in the list", 100, True]
</pre>
## How to access item in the list?
The list of item in the python can be accessed by giving position of a item found in the list which is called index.
e.g
<pre>
Car_name = ["Toyota", "Tesla", "BYD"]
print(Car_name[0]) // so 0 is an index to return Toyota from the list.
print(Car_name[0].upper()) #we can apply string method to this index because its string data, we can do to other also becasue other also have string data type.
</pre>
<pre>
Toyota
TESLA
</pre>
**Remember** 
In python index always start from the 0, not 1, first item position index is 0 then continue.
## Using Individual item from the list 
Individual item from the list, we can access, maninpulte and apply method to them as a variable.
we can apply f-string and other formating string, we can maninpute using string method such as lower(), upper(), title,strip etc.
e.g 
<pre>
PL_list = ["Java", "----Javascript------", "Python"]
print(PL_list[0])
print(PL_list[1].strip("-"))
print(f"I am one the the most windly used programming language {PL_list[2]})
</pre>
Output: 
<pre>
Java
Javascript
Python
</pre>
## Manipulating list
### Modifiying, Adding, Removing
*Modefying*  in python we can modifiy the value of items in the list.
we modifiy a list of items in the same way with accessing but assign the value after accessed immediatly.
e.g <pre>
PC_Brands = ["Toshiba", "Dell", "Mac"]
print(PC_Brands) #displaying the list before modified.

PC_Brands[0] = "Hp"
print(PC_Brands) #Toshiba is modified to Hp
</pre>
Output: 
<pre>
['Toshiba', 'Dell', 'Mac']
['Hp', 'Dell', 'Mac']
</pre>

### Adding
Adding in python, we can add item value in to list in two ways using append() and insert() method.
*append()*, using append method we can add item value to the end of the list, it simplest one.
e.g 
<pre>
Mobile_Brands =["Iphone", "Samsung", "Huawei"]
print(Mobile_Brands) #Display before new item value is added.

Mobile_Brands.append("ZTE") #Add ZTE brands in the end of the list of Mobile_Brands.
print(Mobile_Brands) #Display after ZTE is add to the end of the list.
</pre>
Output: 
<pre>
['Iphone', 'Samsung', 'Huawei']
['Iphone', 'Samsung', 'Huawei', 'ZTE']
</pre>

**insert()* method, using insert method we can add value it any specific index on the lists, insert(new_Value, index).
e.g 
<pre>
Mobile_Brands = ["Nokia", "Techno", "BlackBerry"]
print(Mobile_Brands) #Orginal list.

Mobile_Brands.insert("Oking", 0)
print(Mobile_Brands) #Display after Oking is inserted into the list in 0 index.
</pre>
Output:
<pre>
['Nokia', 'Techno', 'BlackBerry']
['Oking', 'Nokia', 'Techno', 'BlackBerry']
</pre>

### Removing
Removing item from list in python there are 3 method used for this purpose, del keyword, remove method and pop method.
**del** is a keyword in python used to delete variable and list item.
e.g 
<pre>
Mobile_Brands = ["Nokia", "Tecno", "LTC"]
print(Mobile_Brands) # Orginal list

del Mobile_Brands[0]
print(Mobile_Brands) # After Nokia removed from the list.
</pre>
Output:
<pre>
['Nokia', 'Techno', 'LTC']
['Techno', 'LTC']
</pre>


**remove()** is a method used to remove item from lists of item form by giving value we wanna to remove from the list.
*remember* remove() delete only first item catched, to remove many we have to loop stemenents.

e.g 
<pre>
Continent_Lists = ["Africa", "Asia", "Europe". "North America", "South America", "Antarctica"]
print(Continent_Lists) # Dispaly orginal list.

Content_Lists.remove("Antarctica")
print(Continent_Lists)
</pre>
Output:
<pre>
['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Antarctica']
['Africa', 'Asia', 'Europe', 'North America', 'South America']
</pre>


**pop()** is a method that used to remove item from end the list by default but we can specifiy value in the parenthese and return value of the removed item, its came from the stack concept.
e.g
<pre>
Brand_Clothes = ['Nike', 'Jordan', 'Puma']
print(Brand_Clothes) # Orignal lists.

removed_value = Brand_Clothes.pop() #storing removed value in new variable called removed_value
print(Brand_Clothes) #displaying after changes.

print(f"I removed {removed_value}, because it is too expensive") #display the removed value.
</pre>
Output:
<pre>
['Nike', 'Jordan', 'Puma']
['Nike', 'Jordan']
I removed Puma, because it is too expensive.
</pre>


## Organizing lists
