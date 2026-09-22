#level 1
#our goal is to read the file, count the words, and count the lines 

#with in with statement tells python to open the file and automatically close it we are done reading it.
with open("sample.txt", "r") as file:
    text = file.read() 

#count the lines
lines = text.splitlines() #splitlines() breaks the text into a list, one iteme per line
lines_count = len(lines)

words = text.split() 
word_count = len(words)

#level 2 

char_count = len(text) #counts every character(spaces and newlines)

char_count_no_space = len(text.replace(" ","")) #this replaces space with no space in the text, so it can count through without spaces 

sentence_count = text.count(".") + text.count("!") + text.count("?") 




print(f"lines: {lines_count}")
print(f"words: {word_count}")
print(f"characters: {char_count}")
print(f"Character(without space): {char_count_no_space}")
print(f"sentence: {sentence_count}")