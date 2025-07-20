'''It Accepts items with the small letter "o" in the new list'''

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
nameswith_o = [item for item in names if 'i'in item]
print(nameswith_o)


'''It Accepts items in new list which have more than 4 letters '''

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
nameswith_o = [item for item in names if (len(item)>4)]
print(nameswith_o)    