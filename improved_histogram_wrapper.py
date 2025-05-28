#!/usr/bin/env python3
"""
Backward compatibility wrapper for improved_histogram.py

This script preserves the original interface of improved_histogram.py
but delegates to the new package implementation.
"""
import sys
from word_histogram.cli import main

if __name__ == "__main__":
    print("NOTE: This script is maintained for backward compatibility.")
    print("Consider using 'word-histogram' or 'python -m word_histogram' instead.\n")
    sys.exit(main())