#!/usr/bin/python3
"""
From unsorted intagers finds a peak.
"""


def search(lo, h, ints):
    """
    searches peak.
    """

    mid = (lo + h) // 2
    if lo == h:
        return ints[h]
    if ints[mid] < ints[mid + 1]:
        return(search(mid + 1, h, ints))
    return(search(lo, mid, ints))


def find_peak(list_of_integers):
    """
    find the peak fro the search
    """

    if not list_of_integers:
        return
    return(search(0, len(list_of_integers) - 1, list_of_integers))
