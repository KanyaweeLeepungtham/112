def extract_words(text):
    words = []
    for w in text.split():
        char = w.strip(" "" ")
        if len(char) >= 4:
            words.append(char)
    return words in text.split if len(char)>=4

print(extract_words("Don't judge a book by its cover."))

print(extract_words("All that glitters is not gold."))

print(extract_words("The multinational corporation's decentralization strategy required comprehensive reorganization of their compartmentalized departmentalization systems across intercontinental subsidiaries."))

