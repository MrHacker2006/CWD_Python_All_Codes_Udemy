

print("5. For deleting all the key value pairs we are using---> .clear()\n")
d1 =  {"Gautam":20, "Rahul":15, "RadheyShyam":1000}
print("Before Using clear()")
print(d1,"\n")

print("After Using clear()")
d1.clear()
print(d1,"\n")




d2 =  {"Gautam":20, "Rahul":15, "RadheyShyam":1000}
print("6. For Removing specific key value pair we are using---> .pop()\n")
d2.pop("Rahul")
print(d2, "\n")



d3 =  {"Gautam":20, "RadheyShyam":1000, "Rahul":15}
print("7.For removing the last key:value pair we are using---> .popitem()")
d3.popitem()
print(d3,"\n")



d4 =  {"Gautam":20, "RadheyShyam":1000, "Rahul":15}
print("8.For removing an item we can also use----> del\n")
del d4['Rahul']
print(d4)




# if key item not mentioned, then it will delete the whole list
d5 =  {"Gautam":20, "RadheyShyam":1000, "Rahul":15}
del d5
print(d5) # Output: NameError: name 'd5' is not defined