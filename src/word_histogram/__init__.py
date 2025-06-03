"""
Word Histogram - A Python tool for analyzing word frequency in text files.
"""

__version__ = "0.1.0"

from .core import count_words, read_text_file
from .exporters import save_to_text, save_to_excel
from .visualization import plot_histogram

__all__ = [
    "count_words",
    "read_text_file",
    "save_to_text",
    "save_to_excel",
    "plot_histogram",
]
