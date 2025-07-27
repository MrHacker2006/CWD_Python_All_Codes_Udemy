
'''''''''Using interseciton()'''''''''''
city1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
city2 = {"Tokyo", "Madrid", "Cannada", "Lucknow"}
city3= city1.intersection(city2)
print(city3,'\n')

'''''''''Using interseciton_update()'''''''''
city1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
city2 = {"Tokyo", "Madrid", "Cannada", "Lucknow"}
city1.intersection_update(city2)
print(city1)