def count_words(text):
    words = text.split()
    return len(words)

def find_word_frequency(text):
    words = text.lower().split()
    
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

def analyze_text(text):
    print(f"Number of characters: {len(text)}")
    print(f"Number of words: {count_words(text)}")
    print("Word frequency:", find_word_frequency(text))

# sample_text = "Hello world. Hello Python. Python is amazing!"
if __name__ == "__main__":
    analyze_text(input())