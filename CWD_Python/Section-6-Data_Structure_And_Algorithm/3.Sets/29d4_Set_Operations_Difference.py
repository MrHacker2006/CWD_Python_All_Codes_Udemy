'''''''Using difference()'''''''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.difference(cities2)
print(cities3)



'''''''Using difference_update()'''''''''
cities3 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities4 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3.difference_update(cities4)
print(cities3)