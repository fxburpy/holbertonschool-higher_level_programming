#!/usr/bin/env python3
"""Module that provides a type-annotated make_multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by a given multiplier."""

    def multiplier_function(number: float) -> float:
        """Multiplies a given float by the multiplier."""
        return number * multiplier

    return multiplier_function
