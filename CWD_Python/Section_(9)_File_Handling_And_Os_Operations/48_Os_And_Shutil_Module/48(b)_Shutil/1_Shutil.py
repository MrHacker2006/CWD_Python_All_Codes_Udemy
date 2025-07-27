import shutil

'''For Copying a File'''
# It will overwrite the content of the file in which we are copying.
# shutil.copy("RadheJi.txt", "KrishnaJi.txt")
# shutil.copy("F1", "F2/")  # Not working for directories


'''For Moving a File or directory'''
# shutil.move("F1.txt", "F2/")  # Movind a file
# shutil.move("F1/", "F2/")       # Moving a directory


'''For Removing an existing directory'''

# shutil.rmtree("F2/")

shutil.copytree("F1/", "F2/")