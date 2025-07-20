# for i in range(1,21):
#     if i == 11:
#         continue    
#     print(i)


'''It skips the line of codes written after it for the particular condition, which is given inside the if statement'''
for i in [2,3,4,5,6,8,0]:
    if(i%2!=0): #Therefore it will not print 3 and 5
        continue
    print(i)