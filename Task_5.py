def word_frequency(text):
    """Return the frequency of each word in the input string as a dictionary."""
    freq = {}
    for word in text.split():
        word = word.lower()
        freq[word] = freq.get(word, 0) + 1
    return freq

if __name__ == "__main__":
    input_str = input("Enter a string: ")
    frequencies = word_frequency(input_str)
    print("Word frequencies:")
    for word, count in frequencies.items():
        print(f"{word}: {count}")
