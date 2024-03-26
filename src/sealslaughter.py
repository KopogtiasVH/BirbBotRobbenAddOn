bad_words_file = '../rsc/bad_words.txt'
score_sheet_file = '../rsc/robben_score_sheet.txt'

bad_words = open(bad_words_file, encoding="utf_8", mode="r").readlines()

def check_message_for_bad_word(str: message):
