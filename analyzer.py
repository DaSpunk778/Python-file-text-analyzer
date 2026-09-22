#level 1
#our goal is to read the file, count the words, and count the lines 

#with tells python to open the file and automatically close it we are done reading it.
with open("sample.txt", "r") as file:
    text = file.read() 

#count the lines
lines = text.splitlines() #splitlines() breaks the text into a list, one iteme per line
lines_count = len(lines)

words = text.split() 
word_count = len(words)

print(f"lines: {lines_count}")
print(f"words: {word_count}")