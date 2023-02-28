import pandas

# TODO 1. Create a dictionary in this format:
#  {"A": "Alfa", "B": "Bravo"}
phonetic_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_data_dict = {row["letter"]: row["code"] for (index, row) in phonetic_data_frame.iterrows()}
print(phonetic_data_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("enter a word to transform to phonetic: ").upper()
word_char_list = [letter for letter in word]
print(word_char_list)

phonetic_name = [phonetic_data_dict[letter] for letter in word_char_list if letter in phonetic_data_dict]

print(phonetic_name)
