import random

#✅ Yes, you can use a tuple instead of a list for storing Millionaire game questions if you're only reading the data (not modifying it).

#But…

#❌ If you plan to shuffle, add, remove, or update questions, then tuple will fail — because it's immutable (cannot be changed after creation).


questions =  [
    ["What is the capital of France?", "Rome", "Madrid", "Paris", "Berlin", 3],
    ["Who developed the theory of relativity?", "Tesla", "Einstein", "Newton", "Darwin", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Saturn", "Jupiter", "Mars", 4],
    ["Which animal is known as the king of the jungle?", "Elephant", "Lion", "Tiger", "Leopard", 2],
    ["What is the boiling point of water?", "80°C", "100°C", "70°C", "90°C", 2],
    ["Which language is used to write Android apps?", "Ruby", "Kotlin", "C", "Swift", 2],
    ["What is the currency of Japan?", "Euro", "Won", "Dollar", "Yen", 4],
    ["Who painted the Mona Lisa?", "Van Gogh", "Picasso", "Da Vinci", "Michelangelo", 3],
    ["What is the hardest natural substance?", "Granite", "Diamond", "Iron", "Gold", 2],
    ["What gas do plants absorb?", "Carbon Dioxide", "Oxygen", "Hydrogen", "Nitrogen", 1],
    ["Which country invented pizza?", "France", "Italy", "Greece", "Spain", 2],
    ["Which ocean is the largest?", "Atlantic", "Indian", "Pacific", "Arctic", 3],
    ["Which instrument has keys, pedals, and strings?", "Piano", "Drums", "Violin", "Guitar", 1],
    ["Who was the first person to walk on the moon?", "Yuri Gagarin", "Buzz Aldrin", "Neil Armstrong", "Michael Collins", 3],
    ["Which element has the symbol 'O'?", "Osmium", "Oxygen", "Olinium", "Oxide", 2],
    ["Which continent is Egypt in?", "Europe", "Africa", "Asia", "Australia", 2],
    ["Who wrote Harry Potter?", "Stephen King", "Jane Austen", "J.K. Rowling", "George R.R. Martin", 3],
    ["Which sport uses a shuttlecock?", "Cricket", "Tennis", "Badminton", "Squash", 3],
    ["Which shape has 3 sides?", "Square", "Circle", "Rectangle", "Triangle", 4],
    ["How many legs does a spider have?", "6", "10", "8", "12", 3]
]
prize=['10$', '20$', '40$', '80$', '160$', '320$', '640$', '1280$', '2560$', '5120$',
 '10240$', '20480$', '40960$', '81920$', '163840$', '327680$', '655360$', '1310720$', '2621440$', '5242880$']
i=0

try:
    random.shuffle(questions)
    for question in questions:
        print(question[0])
        print(f"a. Enter 1 for {question[1]}")
        print(f"b. Enter 2 for {question[2]}")
        print(f"c. Enter 3 for {question[3]}")
        print(f"d. Enter 4 for {question[4]}")

        # Checking whethter the answer is correct or not.
        a = int(input("Enter the number of the correct option : \n"))
        if question[5]==a:
            print("Your answer is correct.")
            print(f"You have won {prize[i]}\n")
        else:
            print(f"You are Incorrect!, the correct answer is {question[5]}")
            print("Better Luck Next Time!")
            break
        i+= 1
except Exception as e:
    print("Please enter an integer from 1 to 4 only.")
