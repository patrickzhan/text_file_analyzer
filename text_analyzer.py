import nltk, os, sys
import seaborn as sns
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Get the current script directory
current_path=os.path.dirname(os.path.abspath(__file__))
nltk_data_path = os.path.join(current_path, 'nltk_data')
if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)

# Set NLTK data search path to the current directory
nltk.data.path.append(nltk_data_path)

# Download NLTK resources
nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)
nltk.download('punkt_tab', download_dir=nltk_data_path)
print(f"\nDEBUG: NLTK data will be saved in: {nltk_data_path}")

#load and clean the text file
def load_and_clean_text(file_path):
    print(f"\nDEBUG: Checking file path: {current_path}/{file_path}")  # Debug log
    if not os.path.exists(file_path):
        print(f"\nDEBUG: File not found: {file_path}")  # Debug log
        return None
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    print(f"\nDEBUG: File content loaded successfully")  # Debug log
    return text

def text_statistics(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    
    total_words = len(words)
    total_sentences = len(sentences)
    avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
    avg_sentence_length = total_words / total_sentences if total_sentences > 0 else 0
    
    print(f"\nTotal Words: {total_words}")
    print(f"\nTotal Sentences: {total_sentences}")
    print(f"\nAverage Word Length: {avg_word_length:.2f}")
    print(f"\nAverage Sentence Length: {avg_sentence_length:.2f} words per sentence")

#Tokenize and Remove Stopwords:
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)  # Split into words
    clean_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return clean_tokens

#Generate Word Frequency:
def get_word_frequency(tokens):
    return Counter(tokens)

# Unique Word Count
def unique_word_count(tokens):
    return len(set(tokens))

#Generate Frequency of a Single Word
def word_frequency(text, target_word):
    # Tokenize the text
    tokens = word_tokenize(text)  # Convert text to lowercase for case-insensitive matching
    # Count word frequencies
    word_counts = Counter(tokens)
    # Get the frequency of the target word
    frequency = word_counts.get(target_word.lower(), 0)
    return frequency

#Visualize the Data
def plot_word_frequency(word_counts, top_n=10):
    common_words = word_counts.most_common(top_n)
    words, counts = zip(*common_words)
    plt.bar(words, counts)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top {top_n} Words')
    plt.xticks(rotation=45)
    plt.show()

def generate_wordcloud(word_counts):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def plot_word_frequency_heatmap(word_counts):
    words, counts = zip(*word_counts.most_common(100))  # Get top 100 words
    heatmap_data = np.array(counts).reshape(10, 10)  # Reshape to 10x10 grid for example
    sns.heatmap(heatmap_data, annot=True, fmt="d", xticklabels=words[:10], yticklabels=words[10:20])
    plt.show()

#main
def main():
    # Check for the argument
    if len(sys.argv) < 2:
        print("Usage: python3 text_analyzer.py <file_path>")
        print("Usage: python3 text_analyzer.py <file_path> <word>")
        sys.exit(1)  # Exit with error code 1 if no argument is provided

    # 1. Load the text file
    file_path = sys.argv[1]
    text = load_and_clean_text(file_path)
    if len(sys.argv)==3:
        special_word=sys.argv[2]

    if text is None:
        print("File not found or could not be read. Exiting.")
        return  # Exit if the file is invalid
  

    # 2. Preprocess the text
    tokens = preprocess_text(text)
    print(f"\nDEBUG: Tokenization complete.")  # Debug log

    # 3. Analyze word frequency
    word_counts = get_word_frequency(tokens)
    unique_word_counts=unique_word_count(tokens)
    word_freq = word_frequency(text, special_word)
    text_statistics(text)

    # 4. Display results
    print(f"\nThe frequency of \"{special_word}\":{word_freq}")
    print("\nTop 10 Words:")
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")
    print(f"\nunique_word_counts:{unique_word_counts}")
    
    # 5. Plot word frequency
    # plot_word_frequency(word_counts, top_n=10)

    # 6. Generate word cloud (optional)
    # generate_wordcloud(word_counts)
    plot_word_frequency_heatmap(word_counts)

if __name__ == "__main__":
    main()

