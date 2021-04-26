 from collections import Counter

def most_repeating_word(words):
word_counts = {word : max(Counter(word).items(),
key=lambda t: t[1]) for word in words}
return max(word_counts, key=lambda w: word_counts[w][1] )