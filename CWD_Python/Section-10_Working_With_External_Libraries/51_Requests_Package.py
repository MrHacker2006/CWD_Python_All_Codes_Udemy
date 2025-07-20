import requests 

r  = requests.get('https://api.github.com/users/MrHacker2006')

print(r.text)

with open("Gatuam_git.txt", "w") as f:
    content = f.write(r.text)