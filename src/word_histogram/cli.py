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
        description="Generate word frequency analysis from text."
    )

    parser.add_argument(
        "input_file",
        nargs="?",
        default="text.txt",
        help="Input text file (default: text.txt)",
    )

    parser.add_argument(
        "--text-output",
        default="out.txt",
        help="Output text file (default: out.txt)",
    )

    parser.add_argument(
        "--excel-output",
        default="out.xlsx",
        help="Output Excel file (default: out.xlsx)",
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=30,
        help="Max words in visualizations (default: 30)",
    )

    parser.add_argument(
        "--no-plot", action="store_true", help="Skip histogram plot display"
    )

    parser.add_argument(
        "--wordcloud", action="store_true", help="Generate word cloud"
    )

    parser.add_argument(
        "--save-plot",
        type=str,
        help="Save plot to file instead of displaying",
    )

    parser.add_argument(
        "--version", action="store_true", help="Show version and exit"
    )

    return parser.parse_args(args)


def _process_file(file_path: Path) -> Optional[List]:
    """Reads the file and counts words."""
    print(f"Analyzing text from '{file_path}'...")
    try:
        text = read_text_file(str(file_path))
        word_counts = count_words(text)
        return word_counts.most_common()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def _save_results(
    sorted_counts: list, text_output_path: str, excel_output_path: str
) -> bool:
    """Handles saving to text and Excel files."""
    try:
        save_to_text(sorted_counts, text_output_path)
        print(f"Text results saved to '{text_output_path}'")

        save_to_excel(sorted_counts, excel_output_path)
        print(f"Excel results saved to '{excel_output_path}'")
        return True
    except Exception as e:
        print(f"Error saving results: {e}")
        return False


def _handle_visualizations(parsed_args: argparse.Namespace, sorted_counts: list):
    """Handles the logic for plotting the histogram and word cloud."""
    if not parsed_args.no_plot:
        try:
            print(
                f"Displaying histogram of the {parsed_args.limit} most common words..."
            )
            plot_histogram(
                sorted_counts, parsed_args.limit, save_path=parsed_args.save_plot
            )
        except Exception as e:
            print(f"Error creating histogram: {e}")

    if parsed_args.wordcloud:
        try:
            print("Generating word cloud visualization...")
            # Assuming save_plot is meant for both or needs adjustment
            # For now, let's consider if wordcloud should have its own save path argument
            # or if save_plot is generic. If generic and wordcloud is also saved,
            # it might overwrite the histogram if names are not distinct.
            # Current implementation of plot_wordcloud and plot_histogram
            # might need review if they both use save_path in a conflicting way.
            # For this refactoring, we'll keep existing logic.
            wordcloud_save_path = parsed_args.save_plot
            if parsed_args.save_plot and parsed_args.no_plot:  # If only wordcloud is saved
                pass  # use default save_plot
            elif parsed_args.save_plot:  # If both might be saved, ensure different names or handle
                # This part might need more sophisticated handling for saving multiple
                # plots. For now, wordcloud will attempt to use the same
                # save_path if provided
                print(
                    "Note: If --save-plot is used for both histogram and "
                    "wordcloud, ensure distinct filenames or one may "
                    "overwrite the other."
                )

            plot_wordcloud(sorted_counts,
                           max_words=parsed_args.limit,
                           save_path=wordcloud_save_path)
        except Exception as e:
            print(f"Error creating word cloud: {e}")


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

    input_path = Path(parsed_args.input_file)
    if not input_path.exists():
        print(f"Error: Input file '{parsed_args.input_file}' not found.")
        return 1

    sorted_counts = _process_file(input_path)
    if sorted_counts is None:
        return 1

    total_unique_words = len(sorted_counts)
    total_words = sum(count for _, count in sorted_counts)
    print(f"Found {total_unique_words} unique words from "
          f"{total_words} total words.")

    if not _save_results(
        sorted_counts, parsed_args.text_output, parsed_args.excel_output
    ):
        return 1

    _handle_visualizations(parsed_args, sorted_counts)

    return 0


if __name__ == "__main__":
    sys.exit(main())
