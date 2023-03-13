import pandas as pd
import random
import os

LANGUAGE_FILE = "data/french_words.csv"
WORDS_TO_LEARN_FILE = "data/words_to_learn.csv"


def check_file():
    if os.path.exists(WORDS_TO_LEARN_FILE):
        data = pd.read_csv(WORDS_TO_LEARN_FILE)
    else:
        data = pd.read_csv(LANGUAGE_FILE)
        data.to_csv(WORDS_TO_LEARN_FILE, index=False)
    return data


class Flashcard:
    def __init__(self):
        self.data = check_file()
        self.card_count = self.data.shape[0]
        self.card_title_language1 = self.data.columns[1]
        self.card_title_language2 = self.data.columns[0]

    def new_card(self, option, current_word):
        word_row = self.data.loc[self.data[self.card_title_language1] == current_word]

        if option == 0:
            words_to_learn_data = pd.read_csv(WORDS_TO_LEARN_FILE)
            words_to_learn_data = words_to_learn_data[words_to_learn_data[self.card_title_language1] != current_word]
            words_to_learn_data.to_csv(WORDS_TO_LEARN_FILE, index=False)

            random_card = random.randint(1, self.card_count - 1)
            card_text_language1 = self.data.iloc[random_card][self.card_title_language1]
            card_text_language2 = self.data.iloc[random_card][self.card_title_language2]
            return self.card_title_language1, card_text_language1, self.card_title_language2, card_text_language2

        if option == 1:
            word_row.to_csv(WORDS_TO_LEARN_FILE, index=False, mode='a', header=not os.path.exists(WORDS_TO_LEARN_FILE))
            random_card = random.randint(1, self.card_count - 1)
            card_text_language1 = self.data.iloc[random_card][self.card_title_language1]
            card_text_language2 = self.data.iloc[random_card][self.card_title_language2]
            return self.card_title_language1, card_text_language1, self.card_title_language2, card_text_language2

    def remove_word(self, word):
        row_to_remove = self.data.loc[self.data[self.card_title_language2] == word]
        self.data.drop(row_to_remove.index, inplace=True)
        self.card_count = self.data.shape[0]  # update card count after removing a word
        self.data.to_csv(LANGUAGE_FILE, index=False)  # update the original CSV file
