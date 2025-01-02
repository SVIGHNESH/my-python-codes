def word_frequency(input_sequence):
    words = input_sequence.split(",")
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    for word, count in frequency.items():
        print(f"{word}:{count}")

input_sequence = input("Enter a comma-separated sequence of word:")
word_frequency(input_sequence)
    
