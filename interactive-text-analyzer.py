"""
Interactive Text Analyzer

This program allows users to analyze text in various ways:
- Count words, characters, and sentences
- Find the most common words
- Search for specific words or phrases
- Calculate readability scores

It demonstrates string manipulation, dictionaries, functions, and user interaction.
"""

def main():
    # Welcome message
    print("\n===== WELCOME TO THE TEXT ANALYZER =====")
    print("This tool helps you analyze any text you provide.")
    
    # Get text from user
    user_text = input("\nEnter or paste the text you want to analyze:\n> ")
    
    while True:
        # Display menu
        print("\nWhat would you like to do with this text?")
        print("1. Count words, characters, and sentences")
        print("2. Find most common words")
        print("3. Search for a word or phrase")
        print("4. Calculate readability statistics")
        print("5. Enter new text")
        print("6. Exit")
        
        # Get user choice
        choice = input("\nEnter your choice (1-6): ")
        
        # Process user choice
        if choice == '1':
            count_text_elements(user_text)
        elif choice == '2':
            word_count = int(input("How many top words would you like to see? "))
            find_common_words(user_text, word_count)
        elif choice == '3':
            search_term = input("Enter the word or phrase to search for: ")
            search_text(user_text, search_term)
        elif choice == '4':
            calculate_readability(user_text)
        elif choice == '5':
            user_text = input("\nEnter or paste the new text:\n> ")
            print("New text has been set!")
        elif choice == '6':
            print("\nThank you for using the Text Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


def count_text_elements(text):
    """Count various elements in the provided text."""
    # Count characters (including spaces)
    char_count = len(text)
    
    # Count characters (excluding spaces)
    char_no_spaces = sum(1 for char in text if char != ' ')
    
    # Count words
    words = text.split()
    word_count = len(words)
    
    # Approximate sentence count based on punctuation
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    # Handle case where there might be no ending punctuation
    if sentence_count == 0 and word_count > 0:
        sentence_count = 1
    
    # Display results
    print("\n----- Text Statistics -----")
    print(f"Total characters (with spaces): {char_count}")
    print(f"Total characters (without spaces): {char_no_spaces}")
    print(f"Total words: {word_count}")
    print(f"Approximate sentence count: {sentence_count}")
    
    # Calculate average word length
    if word_count > 0:
        avg_word_length = sum(len(word) for word in words) / word_count
        print(f"Average word length: {avg_word_length:.2f} characters")
    
    # Calculate average sentence length
    if sentence_count > 0:
        avg_sentence_length = word_count / sentence_count
        print(f"Average sentence length: {avg_sentence_length:.2f} words")


def find_common_words(text, count=5):
    """Find and display the most common words in the text."""
    # Clean and split text
    # Remove punctuation and convert to lowercase for better counting
    clean_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)
    words = clean_text.split()
    
    # Count word frequencies
    word_freq = {}
    for word in words:
        if len(word) > 1:  # Ignore single-letter words (often articles or prepositions)
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort words by frequency
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    # Display results
    print("\n----- Most Common Words -----")
    if not sorted_words:
        print("No words found in the text.")
        return
    
    # Limit to requested count
    show_count = min(count, len(sorted_words))
    for i in range(show_count):
        word, freq = sorted_words[i]
        print(f"{i+1}. '{word}' appears {freq} times")


def search_text(text, search_term):
    """Search for a specific word or phrase in the text."""
    # Convert to lowercase for case-insensitive search
    text_lower = text.lower()
    search_term_lower = search_term.lower()
    
    # Count occurrences
    count = text_lower.count(search_term_lower)
    
    # Find positions
    positions = []
    start_pos = 0
    while start_pos < len(text_lower):
        pos = text_lower.find(search_term_lower, start_pos)
        if pos == -1:
            break
        positions.append(pos)
        start_pos = pos + 1
    
    # Display results
    print(f"\n----- Search Results for '{search_term}' -----")
    print(f"Found {count} occurrence(s)")
    
    if count > 0:
        # Show context for each occurrence
        for i, pos in enumerate(positions):
            # Get context (up to 20 chars before and after)
            start = max(0, pos - 20)
            end = min(len(text), pos + len(search_term) + 20)
            
            # Extract the context
            context = text[start:end]
            
            # Add ellipsis if needed
            if start > 0:
                context = "..." + context
            if end < len(text):
                context = context + "..."
            
            # Highlight the search term in the context (using a simple approach)
            # First, find the term's position in this context string
            term_pos_in_context = pos - start if start < pos else 0
            
            # Split the context into parts
            before = context[:term_pos_in_context]
            term = context[term_pos_in_context:term_pos_in_context+len(search_term)]
            after = context[term_pos_in_context+len(search_term):]
            
            # Print with the term highlighted (using asterisks for emphasis)
            print(f"\n{i+1}. {before}*{term}*{after}")


def calculate_readability(text):
    """Calculate and display readability metrics."""
    # Count words, sentences, and syllables
    words = text.split()
    word_count = len(words)
    
    # Count sentences (approximate)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    if sentence_count == 0 and word_count > 0:
        sentence_count = 1
    
    # Count syllables (very approximate)
    # A more accurate syllable counter would use a dictionary or complex rules
    def count_syllables(word):
        word = word.lower()
        # Remove punctuation from word
        word = ''.join(char for char in word if char.isalpha())
        
        # Count vowel groups
        vowels = "aeiouy"
        count = 0
        prev_is_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not prev_is_vowel:
                count += 1
            prev_is_vowel = is_vowel
        
        # Adjust count for some common patterns
        if word.endswith('e') and not word.endswith('le'):
            count -= 1
        if count == 0:  # Ensure every word has at least one syllable
            count = 1
        
        return count
    
    total_syllables = sum(count_syllables(word) for word in words)
    
    # Calculate readability scores if there's enough text
    print("\n----- Readability Statistics -----")
    if word_count == 0 or sentence_count == 0:
        print("Not enough text to calculate readability.")
        return
    
    # Average words per sentence
    avg_words_per_sentence = word_count / sentence_count
    print(f"Average words per sentence: {avg_words_per_sentence:.2f}")
    
    # Average syllables per word
    avg_syllables_per_word = total_syllables / word_count
    print(f"Average syllables per word: {avg_syllables_per_word:.2f}")
    
    # Flesch-Kincaid Reading Ease
    # Higher scores = easier to read (90-100: 5th grade, 60-70: 8th-9th grade, 0-30: college graduate)
    flesch_reading_ease = 206.835 - (1.015 * avg_words_per_sentence) - (84.6 * avg_syllables_per_word)
    print(f"Flesch Reading Ease: {flesch_reading_ease:.2f}")
    
    # Interpret the score
    if flesch_reading_ease >= 90:
        reading_level = "Very Easy (5th grade)"
    elif flesch_reading_ease >= 80:
        reading_level = "Easy (6th grade)"
    elif flesch_reading_ease >= 70:
        reading_level = "Fairly Easy (7th grade)"
    elif flesch_reading_ease >= 60:
        reading_level = "Standard (8th-9th grade)"
    elif flesch_reading_ease >= 50:
        reading_level = "Fairly Difficult (10th-12th grade)"
    elif flesch_reading_ease >= 30:
        reading_level = "Difficult (College)"
    else:
        reading_level = "Very Difficult (College Graduate)"
    
    print(f"Approximate reading level: {reading_level}")


# Run the program when the script is executed
if __name__ == "__main__":
    main()
