# Usage Guide

## Introduction

Word Histogram is a Python tool for analyzing word frequency in text files. It provides functionality to count word occurrences, generate visualizations, and export results to different formats.

## Installation

### Using pip

The easiest way to install Word Histogram is via pip:

```bash
pip install word-histogram
```

### From Source

You can also install from source:

```bash
git clone https://github.com/username/word-histogram.git
cd word-histogram
pip install .
```

### Development Installation

For development, install in editable mode with optional dependencies:

```bash
git clone https://github.com/username/word-histogram.git
cd word-histogram
pip install -e ".[dev,wordcloud]"
```

## Command-line Interface

Word Histogram provides a command-line interface for quick analysis of text files.

### Basic Usage

```bash
# Analyze a text file with default settings
word-histogram mytext.txt

# Analyze using the module interface
python -m word_histogram mytext.txt
```

### Command-line Options

| Option | Description |
|--------|-------------|
| `input_file` | Text file to analyze (default: text.txt) |
| `--text-output FILE` | Output text file path (default: out.txt) |
| `--excel-output FILE` | Output Excel file path (default: out.xlsx) |
| `--limit N` | Limit the number of words in visualizations (default: 30) |
| `--no-plot` | Skip displaying the histogram plot |
| `--wordcloud` | Generate a word cloud visualization (requires wordcloud package) |
| `--save-plot FILE` | Save the plot to a file instead of displaying it |
| `--version` | Show version information and exit |

### Examples

```bash
# Analyze a custom file
word-histogram path/to/mynovel.txt

# Export to custom output files
word-histogram input.txt --text-output results.txt --excel-output results.xlsx

# Display only the top 20 words
word-histogram input.txt --limit 20

# Save the plot instead of displaying it
word-histogram input.txt --save-plot histogram.png

# Generate a word cloud
word-histogram input.txt --wordcloud

# Don't show any plots
word-histogram input.txt --no-plot
```

## Python API

You can also use Word Histogram programmatically in your Python code.

### Basic Usage

```python
from word_histogram.core import read_text_file, count_words
from word_histogram.exporters import save_to_text, save_to_excel
from word_histogram.visualization import plot_histogram

# Read the text file
text = read_text_file("mytext.txt")

# Count word occurrences
word_counts = count_words(text)

# Get the most common words
top_words = word_counts.most_common(10)
for word, count in top_words:
    print(f"{word}: {count}")

# Save results to files
save_to_text(word_counts.most_common(), "results.txt")
save_to_excel(word_counts.most_common(), "results.xlsx")

# Generate a histogram visualization
plot_histogram(word_counts.most_common(), limit=20)
```

### Core Functions

#### `read_text_file(file_path)`

Reads text from a file.

```python
from word_histogram.core import read_text_file

text = read_text_file("mytext.txt")
```

#### `count_words(text)`

Cleans text and counts word occurrences.

```python
from word_histogram.core import count_words

word_counts = count_words("This is a sample text. This text has repeated words.")
print(word_counts)  # Counter({'this': 2, 'text': 2, 'is': 1, 'a': 1, ...})
```

### Export Functions

#### `save_to_text(word_counts, output_file)`

Saves word counts to a text file.

```python
from word_histogram.exporters import save_to_text

save_to_text([("word1", 10), ("word2", 5)], "results.txt")
```

#### `save_to_excel(word_counts, output_file)`

Saves word counts to an Excel file.

```python
from word_histogram.exporters import save_to_excel

save_to_excel([("word1", 10), ("word2", 5)], "results.xlsx")
```

### Visualization Functions

#### `plot_histogram(word_counts, limit=30, title='Word Frequency Histogram')`

Creates and displays a histogram of the most common words.

```python
from word_histogram.visualization import plot_histogram

plot_histogram([("word1", 10), ("word2", 5)], limit=20)
```

#### `plot_wordcloud(word_counts, max_words=100)`

Creates and displays a word cloud visualization (requires the wordcloud package).

```python
from word_histogram.visualization import plot_wordcloud

plot_wordcloud([("word1", 10), ("word2", 5)], max_words=50)
```

## Troubleshooting

### Common Issues

#### ImportError: No module named 'openpyxl'

Excel export functionality requires the openpyxl package:

```bash
pip install openpyxl
```

#### ImportError: No module named 'wordcloud'

Word cloud visualization requires the wordcloud package:

```bash
pip install wordcloud
```

#### File Not Found Error

Ensure that the input file path is correct and the file exists.

#### Unicode Decode Error

If you encounter issues with text encoding, try specifying the encoding when reading the file:

```python
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
```

For more complex issues, please refer to the [GitHub repository](https://github.com/username/word-histogram/issues) for known issues or to report new ones.