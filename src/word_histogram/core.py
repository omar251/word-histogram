"""
Core functionality for word histogram generation.
"""
import re
from collections import Counter
from pathlib import Path


def read_text_file(file_path):
    """
    Read and return text from a file.
    
    Args:
        file_path (str or Path): Path to the text file to read
        
    Returns:
        str: Content of the text file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def count_words(text):
    """
    Clean text and count word occurrences.
    
    Args:
        text (str): Text to analyze
        
    Returns:
        Counter: Dictionary-like object with words as keys and counts as values
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = re.sub(r"[^a-z0-9 ]", "", text.lower())
    words = cleaned_text.split()
    
    # Count occurrences using Counter (much more efficient)
    return Counter(words)