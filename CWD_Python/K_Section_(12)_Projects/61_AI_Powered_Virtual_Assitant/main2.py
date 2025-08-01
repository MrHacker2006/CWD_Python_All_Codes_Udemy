from google import genai
client = genai.Client(api_key="AIzaSyBe9QXYL4Ylue9CC") # Write your own API key , the key written here is not valid
questions = ["ask away"] 
print ("Let's start this conversation\n")
for q in questions:
        question = input("At any point to end this chat type Exit\n")     
        if question == "Exit":         
            break     
        else:        
             questions.append(question)   
             response = client.models.generate_content(model="gemini-2.5-flash",contents= question, )         
             print(response.text)  
