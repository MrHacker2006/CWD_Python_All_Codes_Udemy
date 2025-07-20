f = open("Gautam2.txt", "w")

lines = ['line1', 'line2', 'line3']  # By Default , writelines() method don't add new line character.
# lines = ['line1\n', 'line2\n', 'line3\n']

f.writelines(lines)

f.close()