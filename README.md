# Word Histogram Generator

A Python tool to analyze word frequency in text files, create visualizations, and export results to different formats.

## Overview

This project provides a complete package to:
- Count word occurrences in text files
- Generate visualizations of word frequencies (histograms and word clouds)
- Export results to both text and Excel formats
- Sort words by frequency of use
- Process text via command-line or Python API

## Installation

### Option 1: Using pip

```bash
# Install the package with all dependencies
pip install -e .

# Install with optional wordcloud support
pip install -e ".[wordcloud]"

# Install for development
pip install -e ".[dev,wordcloud]"
```

### Option 2: Using UV (faster)

```bash
# Install dependencies using UV
uv pip install -e .
```

## Usage

### Command-line Interface

```bash
# Basic usage with default files
word-histogram

# Specify a different input file
word-histogram my_text.txt

# Customize output files
word-histogram --text-output results.txt --excel-output results.xlsx

# Limit the number of words in the histogram
word-histogram --limit 20

# Generate a word cloud (requires wordcloud package)
word-histogram --wordcloud

# Save plot to file instead of displaying
word-histogram --save-plot histogram.png
```

### Python API

```python
from word_histogram.core import read_text_file, count_words
from word_histogram.exporters import save_to_text, save_to_excel
from word_histogram.visualization import plot_histogram

# Read and analyze text
text = read_text_file("mytext.txt")
word_counts = count_words(text)

# Get most common words
top_words = word_counts.most_common(10)
for word, count in top_words:
    print(f"{word}: {count}")

# Save results
save_to_text(word_counts.most_common(), "results.txt")
save_to_excel(word_counts.most_common(), "results.xlsx")

# Visualize results
plot_histogram(word_counts.most_common(), limit=20)
```

## Features

- **Text Processing**: Cleans and normalizes text for analysis
- **Efficient Word Counting**: Uses Python's Counter for optimal performance
- **Visualization**: Creates bar charts and word clouds
- **Multiple Output Formats**: Exports to plain text and Excel formats
- **Command-line Interface**: Easy to use CLI with various options
- **Python API**: Programmatic access to all functionality
- **Sample Data**: Includes sample text for testing
- **Comprehensive Documentation**: Detailed usage guide and API reference

## Project Structure

```
word-histogram/
├── docs/               # Documentation
├── examples/           # Example scripts
├── src/                # Source code
│   └── word_histogram/ # Main package
├── tests/              # Unit tests
└── ...
```

## Dependencies

- matplotlib: For visualization
- openpyxl: For Excel file generation
- wordcloud (optional): For word cloud visualization
- Python 3.10+: For modern language features