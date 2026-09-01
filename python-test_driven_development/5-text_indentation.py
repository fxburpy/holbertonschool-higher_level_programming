#!/usr/bin/python3
"""Provide a function that formats text around punctuation."""


def text_indentation(text):
    """Print text with two newlines after period, question mark, or colon."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for character in text:
        if character in ".?:":
            line += character
            print(line.strip())
            print()
            line = ""
        elif line or character != " ":
            line += character
    if line:
        print(line.strip(), end="")
