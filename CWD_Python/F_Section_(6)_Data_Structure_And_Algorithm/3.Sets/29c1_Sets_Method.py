
print("1.Using add()")     # It will simply add an element to the set
city1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
city1.add("Kanpur")
print(city1,"\n")


print("2.Using update()")  # Use when you want to add more than one item
city2 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
city2a = {"Kanpur", "Lucknow", "Agra", "Ayodhya"}
city2.update(city2a)
print(city2, "\n")


print("3a.Using remove()")  # Use when you are sure that, the item which you are deleting is present in the list
city3 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
city3.remove("Tokyo")
print(city3, "\n")


''' It will Throw an error, because the element which we are removing (Kanpur)is not present in the set. That's why discard() is preffered over remove(), because it's don't any error still if the intended element is not present'''

# print("3b.Using remove()") 
# city3 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# city3.remove("Kanpur")
# print(city3, "\n")


print("4.Using discard()")
city4 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
city4.discard("Kanpur")
print(city4, "\n")


print("5.Using discard()")
city5 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
city5.pop()
print(city5,"\n")