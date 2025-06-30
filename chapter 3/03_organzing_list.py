#In python there are different of ways of organzing list, such as arranging the list in ascending order, descending order, reverse and etc, using e.g sort(), sorted() and other method.

#sort is a method used to arrange a list in ascending or descending order permantly.
#e.g using sort()
English_Alphabets_list = ['g', 'z', 'a', 'f', 'c']
print(English_Alphabets_list()) # Display the orginal list.

English_Alphabets_list.sort() #sort in ascending order the list permantly.
print(English_Alphabets_list) # Display sort in ascending ordered list.

English_Alphabets_list.sort(reverse = True) # sort in descending order permanly.
print(English_Alphabets_list) # Display the list in descending ordered list.

#sorted is them same with sort method but only difference is sorted method is only change the list item temporary not permanly.
# e.g using sorted

Numbers_list = [66,2,63,35,77,1,3,75,7]
print(Numbers_list) # Display orginal list.

print(Numbers_list.sorted()) # Display sorted list in ascending order temporary.
print(Numbers_list.sorted(reverse = True)) # Display sorted list in descending order temporary.
print(Numbers_list) # Display the orignal list, because, Back to the orginal list.

#reverse is another method used to reverse the the order of the orignal list permantly, but we can back it to the original by using reverse method again after reversed.
#e.g reverse the original list using reverse() method.

Car_Brands = ["Tesla", "Toyota", "BYD", "Suzuki"]
print(Car_Brands) # Display the original lists.
 
Car_Brands.reverse() #reversed the original list.
print(Car_Brands) # Display the reversed list.

Car_Brands.reversed() #reversed the the reversed list again which equal with origal list.
print(Car_Brands) # Display the orginal list again.