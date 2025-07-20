class Animal:
    location="Australia"

    def __init__(self, name):
        self.name=name

    def speak(self):
        print("Speaking Now....")
 
    def name(self, name):
        print(f"The name of the Animal is {self.name}")

    

class Dog(Animal):
    def speak(self):
        super().speak() #From this---> we can use the speak() function of the parent class
        print("Woof!")


d = Dog("Bruno")
d.speak()
# d.name()  # It is giving error, don't know why
print(d.location)