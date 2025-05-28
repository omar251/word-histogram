"""
Visualization functionality for word histogram data.

This module provides functions to create visualizations
of word frequency data using matplotlib.
"""
from typing import List, Tuple, Optional
import matplotlib.pyplot as plt


def plot_histogram(word_counts: List[Tuple[str, int]], limit: int = 30, 
                   title: str = 'Word Frequency Histogram', 
                   figsize: Tuple[int, int] = (12, 8),
                   save_path: Optional[str] = None) -> None:
    """
    Create and display a histogram of the most common words.
    
    Args:
        word_counts: List of (word, count) tuples, typically from Counter.most_common()
        limit: Maximum number of words to include in the visualization
        title: Title of the plot
        figsize: Figure size as (width, height) in inches
        save_path: If provided, save the figure to this path instead of displaying
        
    Returns:
        None
    """
    # Limit to top N words for readability
    top_words = word_counts[:limit]
    
    if not top_words:
        print("No words to display in histogram")
        return
        
    words, counts = zip(*top_words)
    
    plt.figure(figsize=figsize)
    y_pos = range(len(words))
    plt.bar(y_pos, counts, align='center', alpha=0.5)
    plt.xticks(y_pos, words, rotation=90)
    plt.ylabel('Frequency')
    plt.title(title)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()


def plot_wordcloud(word_counts: List[Tuple[str, int]], 
                   max_words: int = 100,
                   figsize: Tuple[int, int] = (10, 10),
                   save_path: Optional[str] = None) -> None:
    """
    Create and display a word cloud visualization.
    
    Note: Requires the wordcloud package to be installed.
    
    Args:
        word_counts: List of (word, count) tuples
        max_words: Maximum number of words to include
        figsize: Figure size as (width, height) in inches
        save_path: If provided, save the figure to this path instead of displaying
        
    Returns:
        None
        
    Raises:
        ImportError: If wordcloud package is not installed
    """
    try:
        from wordcloud import WordCloud
    except ImportError:
        print("WordCloud visualization requires the wordcloud package.")
        print("Install it with: pip install wordcloud")
        return
        
    # Convert to dictionary format required by WordCloud
    word_dict = dict(word_counts[:max_words])
    
    plt.figure(figsize=figsize)
    wordcloud = WordCloud(width=800, height=800, 
                          background_color='white',
                          max_words=max_words).generate_from_frequencies(word_dict)
                          
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()