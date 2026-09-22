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

#level 3

#we started with an assumption which updates after the confition check
longest_word = words[0]
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

shortest_word = words[0]
for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word

#for counting a specific word 
target_word = "python"
count = 0
for word in words:
    if word == target_word:
        count = count + 1





print(f"lines: {lines_count}")
print(f"words: {word_count}")
print(f"characters: {char_count}")
print(f"Character(without space): {char_count_no_space}")
print(f"sentence: {sentence_count}")
print(f'"{target_word}" appears: {count} times')
