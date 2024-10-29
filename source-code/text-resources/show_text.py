#!/usr/bin/env python

import importlib.resources


text = importlib.resources.read_text('utils', 'text_data.txt')
print(text)
