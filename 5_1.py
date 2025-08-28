sentence = "Anan and Benjawan want to play badminton before dinner."
words = []
word = ""
for ch in sentence:
    if ch == " ":
        if word != "":
            words.append(word)
            word = ""
    else:
        if "A" <= ch <= "Z":
            word += chr(ord(ch) + 32)
        else:
            word += ch
if word:
    words.append(word)
print(words)
print("Number of words:", len(words))

# sentence = "It's suggested to walk, study, and sleep everyday; for a great health."
#
# separators = [" ", ",", ";", ":"]
#
# words = []
# word = ""
# for ch in sentence:
#     if ch in separators:
#         if word != "":
#             words.append(word)
#             word = ""
# if word:
#     words.append(word)
# print(words)
# print("Number of words:", len(words))
