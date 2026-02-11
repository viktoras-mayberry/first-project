"""
Utility functions for the Hospital Patient Queue Management System.
"""
from __future__ import annotations


def get_int_input(prompt: str, default: int | None = None) -> int:
    """
    Read an integer from user input. Retries until valid.

    Args:
        prompt: Message to display.
        default: Optional default value if user enters nothing.

    Returns:
        The integer entered by the user (or default).
    """
    while True:
        raw = input(prompt).strip()
        if default is not None and raw == "":
            return default
        try:
            return int(raw)
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_choice(prompt: str, valid: set[str] | None = None) -> str:
    """
    Read a non-empty string choice from user input.

    Args:
        prompt: Message to display.
        valid: Optional set of allowed values (case-insensitive).

    Returns:
        The trimmed string entered by the user.
    """
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("Please enter a value.")
            continue
        if valid is not None and raw.lower() not in {v.lower() for v in valid}:
            print(f"Invalid choice. Allowed: {', '.join(sorted(valid))}")
            continue
        return raw
