import string

def process_text(text):
   
    translator = str.maketrans('', '', string.punctuation)
    processed_text = text.translate(translator).lower()
    return processed_text

def calculate_frequency(text):
    words = text.split()
    word_frequency = {}

    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    return word_frequency

def display_frequency_distribution(word_frequency):
    sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True))

    for word, frequency in sorted_word_frequency.items():
        print(f"{word}: {frequency}")

def main():
    
    with open("sample_text.txt", "r") as file:
        text = file.read()


    processed_text = process_text(text)

    
    word_frequency = calculate_frequency(processed_text)
    print("Frequency Distribution of Words:")
    display_frequency_distribution(word_frequency)

if __name__== "_main_":
    main()
