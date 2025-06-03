#!/usr/bin/env python3
"""
Main entry point for running the package as a module.

This allows running the package with:
    python -m word_histogram
"""
import sys
from word_histogram.cli import main

if __name__ == "__main__":
    sys.exit(main())
