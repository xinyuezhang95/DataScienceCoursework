# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 12:25:18 2024

@author: zxy23
"""

import pandas as pd

nato_df = pd.read_csv('nato_phonetic_alphabet.csv')

# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_dict = {
    row.letter: row.code for (index, row) in nato_df.iterrows()
    }

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input('Enter a word: ').upper()
result = [nato_dict[letter] for letter in user_input]
print(result)

