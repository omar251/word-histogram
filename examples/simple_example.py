#!/usr/bin/env python3
"""
Simple example script demonstrating the use of the word_histogram package.

This example reads a sample text file, analyzes word frequency,
and demonstrates various outputs and visualizations.
"""
import os
from pathlib import Path

# Import functionality from the word_histogram package
from word_histogram.core import read_text_file, count_words
from word_histogram.exporters import save_to_text, save_to_excel
from word_histogram.visualization import plot_histogram

# Get the path to the sample file in the examples directory
current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
sample_file = current_dir / "sample.txt"

# Step 1: Read the sample text file
print(f"Reading text from {sample_file}")
text = read_text_file(sample_file)
print(f"Read {len(text)} characters")

# Step 2: Count word occurrences
word_counts = count_words(text)
print(f"Found {len(word_counts)} unique words")

# Step 3: Get the most common words
top_words = word_counts.most_common(10)
print("\nTop 10 words:")
for word, count in top_words:
    print(f"  {word}: {count}")

# Step 4: Save results to text file
output_txt = current_dir / "word_counts.txt"
save_to_text(word_counts.most_common(), output_txt)
print(f"\nSaved text results to {output_txt}")

# Step 5: Save results to Excel file
output_xlsx = current_dir / "word_counts.xlsx"
save_to_excel(word_counts.most_common(), output_xlsx)
print(f"Saved Excel results to {output_xlsx}")

# Step 6: Generate a histogram plot
print("\nGenerating histogram plot...")
plot_histogram(
    word_counts.most_common(), 
    limit=15,
    title="Word Frequency in Sample Text"
)

print("\nExample completed!")