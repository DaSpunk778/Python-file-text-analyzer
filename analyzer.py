# level 1
def count_lines(text):
    lines = text.splitlines()
    return len(lines)

def count_words(text):
    words = text.split()
    return len(words)

# level 2
def char_sent(text):
    char_count = len(text)
    char_count_no_space = len(text.replace(" ", ""))
    sentence_count = text.count(".") + text.count("!") + text.count("?")
    return char_count, char_count_no_space, sentence_count

# level 3
def long_short(words):
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    shortest_word = words[0]
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word

    return longest_word, shortest_word

def count_target(words, target_word):
    count = 0
    for word in words:
        if word == target_word:
            count += 1
    return count


# --- Main program: read the file, then call every function ---
with open("sample.txt", "r") as file:
    text = file.read()

words = text.split()   # build this once here, since multiple functions need it

lines_count = count_lines(text)
word_count = count_words(text)
char_count, char_count_no_space, sentence_count = char_sent(text)
longest_word, shortest_word = long_short(words)

target_word = "python"
target_count = count_target(words, target_word)

print(f"lines: {lines_count}")
print(f"words: {word_count}")
print(f"characters: {char_count}")
print(f"Character(without space): {char_count_no_space}")
print(f"sentence: {sentence_count}")
print(f"Longest word: {longest_word}")
print(f"Shortest word: {shortest_word}")
print(f'"{target_word}" appears: {target_count} times')