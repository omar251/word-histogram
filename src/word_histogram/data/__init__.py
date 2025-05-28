"""
Data package for word_histogram.

This package contains sample text files and other data resources used by the word_histogram package.
"""

import os
from pathlib import Path

# Get the path to the data directory
DATA_DIR = Path(os.path.dirname(os.path.abspath(__file__)))

def get_sample_text_path():
    """Return the path to the sample text file."""
    return DATA_DIR / "sample.txt"

def load_sample_text():
    """Load and return the contents of the sample text file."""
    with open(get_sample_text_path(), 'r', encoding='utf-8') as f:
        return f.read()