#!/usr/bin/env python3
"""
Unit tests for the Word Histogram Generator.
"""
import os
import tempfile
import unittest
from collections import Counter
from pathlib import Path

# Import functions from the word_histogram package
from word_histogram.core import read_text_file, count_words
from word_histogram.exporters import save_to_text, save_to_excel


class TestWordHistogram(unittest.TestCase):
    """Test cases for the Word Histogram Generator."""

    def setUp(self):
        """Set up test environment."""
        # Create a temporary file with test text
        self.test_text = "This is a test. This test has repeated words, words, words!"
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.temp_dir.name)
        
        # Create input file
        self.input_file = self.temp_path / "test_input.txt"
        with open(self.input_file, "w", encoding="utf-8") as f:
            f.write(self.test_text)
            
        # Define output files
        self.text_output = self.temp_path / "test_output.txt"
        self.excel_output = self.temp_path / "test_output.xlsx"

    def tearDown(self):
        """Clean up after tests."""
        self.temp_dir.cleanup()

    def test_read_text_file(self):
        """Test reading text from a file."""
        result = read_text_file(self.input_file)
        self.assertEqual(result, self.test_text)

    def test_count_words(self):
        """Test counting words in text."""
        result = count_words(self.test_text)
        
        # Expected word counts
        expected = Counter({
            "this": 2,
            "is": 1,
            "a": 1,
            "test": 2,
            "has": 1,
            "repeated": 1,
            "words": 3
        })
        
        self.assertEqual(result, expected)
        
        # Check most common words
        most_common = result.most_common(2)
        self.assertEqual(most_common[0][0], "words")
        self.assertEqual(most_common[0][1], 3)

    def test_save_to_text(self):
        """Test saving word counts to a text file."""
        word_counts = [("words", 3), ("this", 2), ("test", 2)]
        save_to_text(word_counts, self.text_output)
        
        # Verify file exists
        self.assertTrue(self.text_output.exists())
        
        # Verify content
        with open(self.text_output, "r", encoding="utf-8") as f:
            content = f.read()
            
        self.assertIn("3         words", content)
        self.assertIn("2         this", content)
        self.assertIn("2         test", content)

    def test_save_to_excel(self):
        """Test saving word counts to an Excel file."""
        word_counts = [("words", 3), ("this", 2), ("test", 2)]
        save_to_excel(word_counts, self.excel_output)
        
        # Verify file exists
        self.assertTrue(self.excel_output.exists())
        
        # We'd need openpyxl to verify content
        # This is a basic test just checking file creation
        self.assertTrue(os.path.getsize(self.excel_output) > 0)

    def test_full_workflow(self):
        """Test the full workflow from text to output files."""
        # Read text
        text = read_text_file(self.input_file)
        
        # Count words
        word_counts = count_words(text)
        sorted_counts = word_counts.most_common()
        
        # Save results
        save_to_text(sorted_counts, self.text_output)
        save_to_excel(sorted_counts, self.excel_output)
        
        # Verify both output files exist
        self.assertTrue(self.text_output.exists())
        self.assertTrue(self.excel_output.exists())


if __name__ == "__main__":
    unittest.main()