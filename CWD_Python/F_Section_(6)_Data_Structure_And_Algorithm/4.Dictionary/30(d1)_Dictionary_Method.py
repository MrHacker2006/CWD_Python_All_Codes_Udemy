d1 =  {"Gautam":20, "Rahul":15, "RadheyShyam":1000}

print("1.Accesing all the keys by using---> .keys()")
print(d1.keys(), "\n")



print("2.Accesing all the values by using ----> .values()")
print(d1.values(), "\n")



print("3.Accesing all the key:value pairs by using ---------> .items()")
print(d1.items(), "\n")



d2 = {"Name":"Gautam", "Age":19}
print("4.Updating the key:value pairs using ---------> .update()")
d2.update({"Age":20})
d2.update({"DOB": 2006})
print(d2)
