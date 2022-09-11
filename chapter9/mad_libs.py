file_path = 'C:/repos/python/automate_the_boring_stuff/chapter9/mad_libs.txt'

words_to_replace = ('ADJECTIVE', 'NOUN', 'ADVERB', 'VERB')
vowels = ('A', 'E', 'I', 'O', 'U')

text = open(file_path).read()
text_words = text.split()

for text_word in text_words:
    for word_to_replace in words_to_replace:
        if word_to_replace in text_word:
            replacement_word = input('Enter ' + ('an ' if word_to_replace[0] in vowels else 'a ') + word_to_replace.lower() + ': ')
            text = text.replace(word_to_replace, replacement_word, 1)

print(text)