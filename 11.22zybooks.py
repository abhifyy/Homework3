"""

Abhmanyu Kidarithil Meethal
PSID:2105385

"""
word_list = input().split()
word_freq = {}
for word in word_list:
    word_freq[word] = word_freq.get(word, 0) + 1
for word in word_list:
    freq = word_freq[word]
    print(word, freq)
