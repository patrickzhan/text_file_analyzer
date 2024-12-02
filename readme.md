# Text Analyzer

This is a Python-based text analysis tool that processes a given text file, analyzes word frequencies, tokenizes the content, generates a word cloud, and visualizes word frequency using both bar charts and heatmaps.

## Features
- **Text Preprocessing**: Tokenizes the text and removes stopwords.
- **Text Statistics**: Provides the total word count, sentence count, average word length, and average sentence length.
- **Word Frequency Analysis**: Counts and displays word frequencies, both overall and for a specific word.
- **Word Frequency Visualization**: Visualizes the frequency of the top words in a bar chart.
- **Word Cloud Generation**: Generates a word cloud of the most frequent words.
- **Heatmap Visualization**: Creates a heatmap to visualize the frequency distribution of the top words.

## Requirements

The following Python packages are required to run the project:

- `nltk`
- `seaborn`
- `numpy`
- `matplotlib`
- `wordcloud`

You can install these dependencies using the following command:

```bash
pip install -r requirements.txt
Installation
Clone this repository or download the files.
Install the required packages by running the command above.
Ensure that the nltk_data directory is created in the same location as the script, as it is required for the NLTK resources to be downloaded.
Usage
Run the script from the command line with the following arguments:

bash
Copy code
python3 text_analyzer.py <file_path> [word]
<file_path>: Path to the text file you want to analyze (e.g., document.txt).
[word] (optional): A specific word you want to get the frequency of in the text.
Example:

bash
Copy code
python3 text_analyzer.py document.txt
python3 text_analyzer.py document.txt example
The first command will analyze the entire text, while the second command will show the frequency of the word "example" in the text.

Output
Text Statistics: Displays the total word count, total sentence count, average word length, and average sentence length.
Word Frequency: Lists the top 10 most frequent words in the text.
Word Frequency for Specific Word: Displays the frequency of the specific word passed as a command-line argument.
Visualizations:
A bar chart showing the top 10 most frequent words.
A word cloud visualization.
A heatmap visualization of the frequency of words.
Example
Given a text file document.txt, running the script as:

bash
Copy code
python3 text_analyzer.py document.txt
Will output something like:

yaml
Copy code
Total Words: 1024
Total Sentences: 56
Average Word Length: 4.53
Average Sentence Length: 18.29 words per sentence

The frequency of "example": 10
Top 10 Words:
the: 134
and: 98
of: 87
to: 65
a: 54
in: 45
...
unique_word_counts: 512
Along with the generated word frequency bar chart, word cloud, and heatmap.

Contributing
If you'd like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request.

License
This project is open source and available under the MIT License.

vbnet
Copy code

### How to Customize:
- Update the project name in the title if necessary.
- You can adjust the usage and example sections based on your script's exact behavior or output.

This `README.md` provides a clear guide for users on how to install, use, and understand the functionality of your text analysis tool.





