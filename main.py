from nltk.corpus import words
word_list = words.words()

for i in word_list:
    print(i)

letters = list(map(str, input().split()))
