animals = [ "cat", 'dog', 'bat', 'mouse','pig', 'horse', 'donkey', 'goat', 'cow']
  #           0      1      2      3       4        5        6       7       8
  #          -9     -8     -7     -6      -5       -4       -3      -2      -1 


'''Note: The element of the end index provided will not be included'''
# print(animals[3:7])
# print(animals[-7:-2])


'''Printing all the elements from a given index till the end'''
# print(animals[2:]) # Using Positive index
# print(animals[-2:]) # Using Negative index


'''Printing all the elements from start to a given index'''
# print(animals[:4])   # Using Positive index
# print(animals[:-3])  # Using Negative index


'''Printing alternate values'''
# print(animals[::2]) 
# print(animals[-8:-1:2])
# print(animals[1:8:3])


'''Printing all the value of list using slicing'''
# print(animals[0:10])   # Using Positive Indexing
# print(animals[-9: ])  # Using Negative Indexing