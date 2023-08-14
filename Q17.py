def main():
 
    file_path = "data.csv"
    try:
        df = pd.read_csv(file_path)
        feedback_data = df["feedback"].tolist()

        
        n = int(input("Enter the number of top frequent words to display: "))

        word_frequency = calculate_word_frequency(feedback_data)

        
        sorted_word_freq = dict(sorted(word_frequency.items(), key=lambda x: x[1], reverse=True))

       
        print(f"\nTop {n} most frequent words:")
        for i, (word, frequency) in enumerate(sorted_word_freq.items()):
            if i >= n:
                break
            print(f"{word}: {frequency}")

     
        top_n_words = list(sorted_word_freq.keys())[:n]
        top_n_frequencies = list(sorted_word_freq.values())[:n]

        plt.bar(top_n_words, top_n_frequencies)
        plt.xlabel("Words")
        plt.ylabel("Frequencies")
        plt.title(f"Top {n} Most Frequent Words")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if _name_ == "_main_":
    main()
