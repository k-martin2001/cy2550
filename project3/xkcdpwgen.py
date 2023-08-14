# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
#kelsey martin
#project 3: password generator

# +
# #!/usr/bin/env python
# -

import argparse
import random

# +
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description = "Generate a secure, memoreable password using the XKCD method")
parser.add_argument('-w', "--words", default=4, help='include WORDS words in the password (default=4)')
parser.add_argument('-c', "--caps", default=0, help='capitalize the first letter of CAPS random words')
parser.add_argument('-n', "--numbers", default=0, help='insert NUMBERS random numbers in the password')
parser.add_argument('-s', "--symbols", default=0, help='insert SYMBOLS random symbols in the password')

args, unknown = parser.parse_known_args()

# +
#import list of words
list_words = open("words.txt").read().splitlines()

#default
pw = ''
def_words = []

#generates words for pw
for i in range(args.words): def_words.append(random.choice(list_words))

#capitalizes words in pw
capitalize = random.sample(def_words, k=args.caps)
for word in def_words:
    pw += word.capitalize() if word in capitalize else word

#adds numbers to pw
for i in range(args.numbers):
    random_id = random.randint(0, len(pw))
    pw = pw[:random_id] + str(random.randint(0, 9)) + pw[random_id:]

#adds symbols to pw
for i in range(args.symbols):
    random_id = random.randint(0, len(pw))
    pw = pw[:random_id] + random.choice("~!@#$%^&*.:;") + pw[random_id:]

print(pw)
# -


