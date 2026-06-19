#!/usr/bin/env python3
"""Module that provides a type-annotated element_length function."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes an iterable of sequences and returns a list of tuples containing

    each sequence and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
