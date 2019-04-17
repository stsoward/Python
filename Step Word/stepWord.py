""HW03.py: This program takes in a word and returns all valid step words"""
__author__ = "Stone Soward" # Your name
__credits__ = ["None"] # Your list of helpers
__email__ = "sowardse@mail.uc.edu" # Your email address

words = open('words.txt', encoding='ascii').read().upper().split()

def step(word):
    """Doctest correct step list given & correct words length
    >>> len(words)
    235886

    >>> step("APPLE")
    ['ALEPPO', 'APPEAL', 'CAPPLE', 'DAPPLE', 'LAPPED', 'LAPPER', 'LAPPET', 'PALPED', 'PAPULE', 'RAPPEL', 'UPLEAP']"""
    word_len = len(word)
    word = word.upper()
    word_dict = {}
    ans = []
    "Create a dictionary with keys being chars in the word"
    for i in range(word_len):
        if word[i] in word_dict.keys():
            word_dict[word[i]] += 1
        else:
            word_dict[word[i]] = 1
    for w in words:
        w_dict = {}
        if len(w) == word_len + 1:
            dif_ltr_ctr = 0
            stop = False
            "Check that every letter in given word is present in possible step word" 
            for k in range(word_len):
                if word[k] not in w:
                    stop = True
            "Check that possible step word has only one new letter (one not in given word)"
            for i in range(len(w)):
                if w[i] not in word:
                    dif_ltr_ctr += 1
            if dif_ltr_ctr < 2 and stop == False:
                "Create a dictionary for the possible step word"
                for i in range(len(w)):
                    if w[i] in w_dict.keys():
                        w_dict[w[i]] += 1
                    else:
                        w_dict[w[i]] = 1
                dict_nt_mtch_ctr = 0
                "Check that the letter count matches or is off by one"
                for j in range(word_len):
                    if w_dict[word[j]] != word_dict[word[j]]:
                        dict_nt_mtch_ctr += 1
                if dict_nt_mtch_ctr == 0 and dif_ltr_ctr == 1:
                    ans.append(w)
                elif dict_nt_mtch_ctr == 1 and dif_ltr_ctr == 0:
                    ans.append(w)
    return ans


def _test():

    import doctest
    doctest.testmod(verbose=True)

if __name__ == "__main__":
    _test()
