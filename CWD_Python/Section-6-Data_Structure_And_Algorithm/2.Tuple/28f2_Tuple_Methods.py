t1 = (2, 3, 4, 55, 3, 23, 54, 67, 3, 3)
#     0  1  2   3  4  5   6   7   8  9

'''For printing indexes of all repeated elements, we can use these ways'''


# Way-1--> Using List Comprehension
indices = [i for i , value in enumerate(t1) if value ==3]
print(indices)
print("\n")



# Way-2--> Using loop
indices = []
for i in range(len(t1)):
    if t1[i] == 3:
        indices.append(i)

print(indices)