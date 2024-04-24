import re
from collections import Counter
from nltk.corpus import stopwords


import nltk
nltk.download('stopwords')


def read_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text


def preprocess_text(text):
    
    text = text.lower()
    # to remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    return text

#  to remove stopwords
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

# to count word frequency
def count_word_frequency(words):
    word_freq = Counter(words)
    return word_freq

# to display word frequency
def display_word_frequency(word_freq):
    for word, freq in word_freq.items():
        print(f'{word}: {freq}')

if __name__ == "__main__":
    # Read text from file
    text = read_text_file("C:/Users/lenov/Downloads/random_paragraphs.txt")

    #to Preprocess text
    processed_text = preprocess_text(text)

    #to Remove stopwords
    filtered_words = remove_stopwords(processed_text)

    # Count word frequency
    word_freq = count_word_frequency(filtered_words)

    #to Display word frequency
    display_word_frequency(word_freq)
