#!/usr/bin/env python

import re
import sys


def word_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = dict()
    words = re.split(r"\W+", text)
    nr_words = 0
    for word in words:
        word = word.lower()
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
        nr_words += 1
    nr_words -= counts.pop("")
    for word, count in counts.items():
        counts[word] /= nr_words
    return counts


if __name__ == "__main__":
    text = " ".join(sys.stdin.readlines())
    counts = word_count(text)
    for word, count in counts.items():
        print(f"{word}: {count}")
