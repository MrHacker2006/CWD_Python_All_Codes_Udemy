import os

'''For Getting Current Working Directory'''
# current_dir = os.getcwd()
# print("Current Directory:",current_dir)


# Mostly all these statements are working one time only, for using them again you have to delete the previously created directories

# '''For Creating a new directory'''
# os.mkdir("New_dir2")   # Create only one level of directory


'''For Creating Nested Directories'''
# os.makedirs("New_dir1/Nested_dir")
# os.makedirs("New_dir2/Nested_dir1/Nested_dir2")


'''For Changing Directory'''
# os.chdir("New_dir2")    # Note able to understand it's meaning.
# current_dir = os.getcwd()
# print("Current Directory:",current_dir)


'''For Listing Current Files and Directories'''
# f = os.listdir(".") #"." it represents current working directory
# print("Current Working Directory:", f)


'''For Removing Files'''
# os.remove("n1.py")
# os.remove("Folder/")   # You will get an error , permission denied


'''For Removing Empty Directory'''
# os.rmdir("New_dir3")


'''For Renaming a file or Directory'''
# os.rename("n1.py","1_Natul1.py")
# os.rename("New_dir2", "New_Dir1")

'''Checking if a file or directory exists or not'''
# print(os.path.exists("1_Natul1.py"))    # True
# print(os.path.exists("New_Dir3"))     # False

# # Join path components in a platform-independent way 
path2 = os.path.join("Folder", "New_Dir1", "file.txt")
print(path2) 