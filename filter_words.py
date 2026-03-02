# Filter Words
# A modified version of https://github.com/gs109111/WordleSolver/blob/dictionary/filter_words.py 

def filter_from_wordlist(word_list):
    # Filter words that are not 5 words
    with open(word_list, "r") as f, open("words_filtered.txt", "w") as f2:
        for line in f:
            if len(line.strip()) == 5: # Remove words with less than or greater than 5 letters
                f2.write(line)
