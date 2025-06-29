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

