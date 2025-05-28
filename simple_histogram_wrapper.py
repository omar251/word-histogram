#!/usr/bin/env python3
"""
Backward compatibility wrapper for simple_histogram.py

This script preserves the original interface of simple_histogram.py
but delegates to the new package implementation.
"""
import argparse
import sys
from pathlib import Path

from word_histogram.core import count_words, read_text_file
from word_histogram.exporters import save_to_excel, save_to_text


def print_top_words(word_counts, limit=10):
    """Print the most common words to the console."""
    print("\nTop words by frequency:")
    print("-" * 30)
    print(f"{'COUNT':<10} {'WORD'}")
    print("-" * 30)
    
    for word, count in word_counts[:limit]:
        print(f"{count:<10} {word}")


def main():
    """Main entry point of the script."""
    parser = argparse.ArgumentParser(description='Generate word frequency data from a text file.')
    parser.add_argument('input_file', nargs='?', default='text.txt', help='Input text file path (default: text.txt)')
    parser.add_argument('--text-output', default='out.txt', help='Output text file path (default: out.txt)')
    parser.add_argument('--excel-output', default='out.xlsx', help='Output Excel file path (default: out.xlsx)')
    parser.add_argument('--limit', type=int, default=10, help='Limit the number of words to display (default: 10)')
    args = parser.parse_args()
    
    print("NOTE: This script is maintained for backward compatibility.")
    print("Consider using 'word-histogram' or 'python -m word_histogram' instead.\n")
    
    # Ensure input file exists
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: Input file '{args.input_file}' not found.")
        return 1
    
    # Process the text
    print(f"Analyzing text from '{args.input_file}'...")
    text = read_text_file(args.input_file)
    word_counts = count_words(text)
    
    # Sort by frequency (most common first)
    sorted_counts = word_counts.most_common()
    
    # Save results
    save_to_text(sorted_counts, args.text_output)
    print(f"Text results saved to '{args.text_output}'")
    
    try:
        save_to_excel(sorted_counts, args.excel_output)
        print(f"Excel results saved to '{args.excel_output}'")
    except ImportError:
        print("Excel output skipped: openpyxl not available")
    
    # Print top words
    print_top_words(sorted_counts, args.limit)
    
    # Summary
    total_unique_words = len(sorted_counts)
    total_words = sum(count for _, count in sorted_counts)
    print(f"\nSummary: Found {total_unique_words} unique words out of {total_words} total words.")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())