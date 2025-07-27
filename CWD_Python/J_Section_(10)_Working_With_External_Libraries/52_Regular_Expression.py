import re

text = "The quick brown fox jumps over the lazy dog."


'''Searching for the first occurence of the word.'''
# match1 = re.search("quick", text)
# if match1:
#     print("Match Found!")
#     print("Starting Index:", match1.start())
#     print("Ending Index:", match1.end())


'''Searching all occurence of a word.'''
# match2= re.findall("the", text, re.IGNORECASE)
# if match2:
#     print("Matches:", match2)


'''Replacing all the occurence of a word'''
# new_text = re.sub("dog", "cat", text)
# print(text,"\n")
# print("dog is replaced by the cat\n")
# print(new_text,"\n")



'''Compile a regex for efficiency (if used multiple times)'''
pattern = re.compile(r"\b\w+\b")  #Matches the whole word
words = pattern.findall(text)
print(text,"\n")
print("Words:", words)

# \b | Word boundary (ensures we match entire words) |
# \w+ | One or more word characters