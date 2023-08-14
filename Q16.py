import string

def preprocess_text(text):
    
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.lower()

def calculate_word_frequency(reviews_data):
    word_freq = {}
    for review in reviews_data:
        processed_review = preprocess_text(review)
        words = processed_review.split()
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    return word_freq

def main():
    
    reviews_data = [
        "This product is amazing and worth every penny.",
        "I didn't like the quality of the product. Disappointed!",
        "The customer service was excellent, but the product was average.",
   
    ]

    word_frequency = calculate_word_frequency(reviews_data)


    sorted_word_freq = dict(sorted(word_frequency.items(), key=lambda x: x[1], reverse=True))

    for word, frequency in sorted_word_freq.items():
        print(f"{word}: {frequency}")

if _name_ == "_main_":
    main()
