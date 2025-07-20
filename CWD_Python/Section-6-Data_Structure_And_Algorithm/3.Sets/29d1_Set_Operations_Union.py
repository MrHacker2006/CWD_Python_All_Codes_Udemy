"""Using Union()"""
# The main difference between union and update() is that union will create a new set but the (Update) will update the previous defined set


city1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
city2 = {"Tokyo", "Madrid", "Cannada", "Lucknow"}
cities3 = city1.union(city2)
print(cities3, '\n')

'''Getting Same Output'''


city4 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
city5 = {"Tokyo", "Madrid", "Cannada", "Lucknow"}
city4.update(city5)
print(city4)
