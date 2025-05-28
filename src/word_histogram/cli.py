#!/usr/bin/env python3
"""
Command-line interface for Word Histogram Generator.

This module provides the main entry point for the command-line application.
"""
import argparse
import sys
from pathlib import Path
from typing import List, Optional

from word_histogram.core import count_words, read_text_file
from word_histogram.exporters import save_to_excel, save_to_text
from word_histogram.visualization import plot_histogram, plot_wordcloud


def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """
    Parse command line arguments.
    
    Args:
        args: Command line arguments to parse (defaults to sys.argv[1:])
        
    Returns:
        Namespace containing the parsed arguments
    """
    parser = argparse.ArgumentParser(
        description='Generate word frequency analysis from a text file.'
    )
    
    parser.add_argument(
        'input_file',
        nargs='?',
        default='text.txt',
        help='Input text file path (default: text.txt)'
    )
    
    parser.add_argument(
        '--text-output',
        default='out.txt',
        help='Output text file path (default: out.txt)'
    )
    
    parser.add_argument(
        '--excel-output',
        default='out.xlsx',
        help='Output Excel file path (default: out.xlsx)'
    )
    
    parser.add_argument(
        '--limit',
        type=int,
        default=30,
        help='Limit the number of words in the visualizations (default: 30)'
    )
    
    parser.add_argument(
        '--no-plot',
        action='store_true',
        help='Skip displaying the histogram plot'
    )
    
    parser.add_argument(
        '--wordcloud',
        action='store_true',
        help='Generate a word cloud visualization'
    )
    
    parser.add_argument(
        '--save-plot',
        type=str,
        help='Save the plot to the specified file instead of displaying it'
    )
    
    parser.add_argument(
        '--version',
        action='store_true',
        help='Show version information and exit'
    )
    
    return parser.parse_args(args)


def main(args: Optional[List[str]] = None) -> int:
    """
    Main entry point for the command-line application.
    
    Args:
        args: Command line arguments (defaults to sys.argv[1:])
        
    Returns:
        Exit code (0 for success, non-zero for errors)
    """
    parsed_args = parse_args(args)
    
    if parsed_args.version:
        from word_histogram import __version__
        print(f"Word Histogram Generator v{__version__}")
        return 0
    
    # Ensure input file exists
    input_path = Path(parsed_args.input_file)
    if not input_path.exists():
        print(f"Error: Input file '{parsed_args.input_file}' not found.")
        return 1
    
    # Process the text
    print(f"Analyzing text from '{parsed_args.input_file}'...")
    try:
        text = read_text_file(parsed_args.input_file)
    except Exception as e:
        print(f"Error reading file: {e}")
        return 1
        
    word_counts = count_words(text)
    
    # Sort by frequency (most common first)
    sorted_counts = word_counts.most_common()
    
    # Print summary
    total_unique_words = len(sorted_counts)
    total_words = sum(count for _, count in sorted_counts)
    print(f"Found {total_unique_words} unique words out of {total_words} total words.")
    
    # Save results
    try:
        save_to_text(sorted_counts, parsed_args.text_output)
        print(f"Text results saved to '{parsed_args.text_output}'")
        
        save_to_excel(sorted_counts, parsed_args.excel_output)
        print(f"Excel results saved to '{parsed_args.excel_output}'")
    except Exception as e:
        print(f"Error saving results: {e}")
        return 1
    
    # Plot visualizations
    if not parsed_args.no_plot:
        try:
            print(f"Displaying histogram of the {parsed_args.limit} most common words...")
            plot_histogram(
                sorted_counts, 
                parsed_args.limit,
                save_path=parsed_args.save_plot
            )
        except Exception as e:
            print(f"Error creating histogram: {e}")
    
    if parsed_args.wordcloud:
        try:
            print("Generating word cloud visualization...")
            plot_wordcloud(
                sorted_counts,
                max_words=100,
                save_path=parsed_args.save_plot
            )
        except Exception as e:
            print(f"Error creating word cloud: {e}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())