student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
data_contents = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in data_contents.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input('Enter a word: ').upper()
def generate_phonetic_alphabet():
    user_input = input('Enter a word: ').upper()
    try:
        nato_word = [nato_alphabet[char] for char in user_input]
    except KeyError:
        print('Sorry, only letters in the alphabet are allowed')
        generate_phonetic_alphabet()
    else:
        print(nato_word)
generate_phonetic_alphabet()