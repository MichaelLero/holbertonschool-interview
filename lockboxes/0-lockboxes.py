#!/usr/bin/python3
"""Module for unlocking lockboxes."""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    unlocked = set([0])  # Start with the first box unlocked
    keys = set(boxes[0])  # Get keys from the first box

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked:
            unlocked.add(key)
            keys.update(boxes[key])  # Add new keys from the unlocked box

    return len(unlocked) == len(boxes)
