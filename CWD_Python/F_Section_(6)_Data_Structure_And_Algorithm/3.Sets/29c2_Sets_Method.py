
print("6. Using isdisjoint()")
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities6 = {"Miami", "Seoul", "Kabul", "Madrid"}      #It will give False, because common element is present in both the sets.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}        #It will give true, because no element is common in both the sets.
cities6 = {"Miami", "Seoul", "Kabul", "Los Angles"}
print(cities.isdisjoint(cities6), '\n')




print("7. Using issuperset()")
cities7 = {"Tokyo", "Madrid", "Berlin", "Delhi"}

cities7a = {"Seoul", "Kabul"}
print(cities7.issuperset(cities7a))  # Should print: False

cities7b = {"Tokyo", "Madrid"}
print(cities7.issuperset(cities7b),"\n")  # Should print: True





print("8.Using issubset()")
city8 =  {"Noida", "Delhi", "Jaipur"}

city8a = {"Noida", "Delhi", "Raipur"} 
print(city8.issubset(city8a))   # Should print: False(because city8 is not a subset of city8a)

city8b = {"Nagpur", "Jaipur", "Gurgaon", "Noida", "Delhi", "Gaziabadh"}
print(city8.issubset(city8b))    # Should print: True(because city8 is a subset of city8b)