"""
Author: Rahul Nanda
September 29, 2017
"""

import requests
import sys
import re
import time
URL = "http://gallows.hulu.com/play?code=nanda7@purdue.edu"


def get_wordlist_filename(word_length):
    if 1 <= word_length <= 4:
        return "google-10000-english-usa-no-swears-short.txt"
    if 5 <= word_length <= 8:
        return "google-10000-english-usa-no-swears-medium.txt"
    return "google-10000-english-usa-no-swears-long.txt"


def first_service_call():
    r = requests.get(URL)
    if r.status_code != 200:
        print ("Initial call to the API: [%s] returned status code:[%d]. Please fix this. Exiting now.." % (URL, r.status_code))
        sys.exit()
    return r.json()


def LAST_RESORT_pick_alphabet_not_picked_yet(letters_guessed):
    """
    This function is called only when we are unable to find any of the unknown words in the
    dictionary files.
    This list is taken from https://www.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
    """
    sequence = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'd', 'l', 'u', 'c', 'm', 'f', 'y', 'w',
                'g', 'p', 'b', 'v', 'k', 'x', 'q', 'j', 'z']
    for alpha in sequence:
        if alpha not in letters_guessed:
            return alpha
    return None


def process_unknown_word(unknown_word, letters_guessed, search_in_complete_dict=False):
    if search_in_complete_dict:
        wordlist_filename = "complete_dict.txt"
    else:
        wordlist_filename = get_wordlist_filename(len(unknown_word))
    wordlist_file_object = open(wordlist_filename, "r")
    alpha_string = "a-z" if len(letters_guessed) == 0 else '^' + ''.join(letters_guessed)

    regex_word = "^" + unknown_word.replace("_", "[%s]" % alpha_string) + "$"
    total_matched_words, position_count = 0, {}
    for i in xrange(len(unknown_word)):
        if unknown_word[i] == '_':
            position_count[i] = {}
    rank = 1
    for dictionary_word in wordlist_file_object:
        dictionary_word = dictionary_word.strip('\n')

        if len(dictionary_word) != len(unknown_word):
            continue
        regex_match_result = re.search(regex_word, dictionary_word, re.IGNORECASE)
        if regex_match_result is not None:
            total_matched_words += 1
            #print dictionary_word
            for i in xrange(len(unknown_word)):
                if unknown_word[i] != '_':
                    continue
                # print dictionary_word[i]
                if not dictionary_word[i].isalpha():
                    continue
                if dictionary_word[i].lower() in position_count[i]:
                    position_count[i][dictionary_word[i].lower()][0] += 1
                    position_count[i][dictionary_word[i].lower()][1] += rank
                else:
                    position_count[i][dictionary_word[i].lower()] = [1, rank]
        rank += 1

    wordlist_file_object.close()
    return position_count, total_matched_words


def generate_guess(current_state, letters_guessed):
    state_words = current_state.split()
    probability_sum = [[chr(ord('a')+i), 0, 0] for i in xrange(26)]
    """
    Now search for the unknown words in the 10,000 wordlist file.
    """
    for unknown_word in state_words:
        # print position_count
        if '_' not in unknown_word:
            continue
        position_count, total_matched_words = process_unknown_word(unknown_word, letters_guessed)
        #print position_count, total_matched_words
        for pos in position_count:
            for alphabet in position_count[pos]:
                probability_sum[ord(alphabet) - ord('a')][1] += \
                    (position_count[pos][alphabet][0] / (1.0 * total_matched_words))
                probability_sum[ord(alphabet) - ord('a')][2] += position_count[pos][alphabet][1]

    probability_sum = sorted(probability_sum, key=lambda ps:ps[1], reverse=True)
    max_probability_val = probability_sum[0][1]

    if max_probability_val == 0:
        """
            this means that no unknown word was found in the 10,000 wordlist files. Now, we should
            search for the unknown words in the complete dictionary file."""
        for unknown_word in state_words:
            # print position_count
            position_count, total_matched_words = process_unknown_word(unknown_word, letters_guessed,
                                                                       search_in_complete_dict=True)

            for pos in position_count:
                for alphabet in position_count[pos]:
                    probability_sum[ord(alphabet) - ord('a')][1] += \
                        (position_count[pos][alphabet][0] / (1.0 * total_matched_words))
                    probability_sum[ord(alphabet) - ord('a')][2] += position_count[pos][alphabet][1]

        probability_sum = sorted(probability_sum, key=lambda ps: ps[1], reverse=True)
        max_probability_val = probability_sum[0][1]


    top_alphabets = []
    for ps in probability_sum:
        if ps[1] == max_probability_val:
            top_alphabets.append(ps)
    # Sort same probability alphabets by the rank in the word frequency dictionary
    top_alphabets = sorted(top_alphabets, key=lambda ta: ta[2])

    if max_probability_val == 0:
        """
        Damn! Still couldn't find the unknown word(s) in the dictionary. Now we just pick alphabets
        in the order of higher probability of occurrence according to the English Text.
        """
        return LAST_RESORT_pick_alphabet_not_picked_yet(letters_guessed)

    #print probability_sum
    #print top_alphabets[0]
    return top_alphabets[0][0]


def play_hangman():

    first_call_dict = first_service_call()
    print first_call_dict
    token, status, current_state = first_call_dict['token'], first_call_dict['status'], first_call_dict['state']
    remaining_guesses = first_call_dict['remaining_guesses']
    letters_guessed = []
    while status == "ALIVE":
        # Let's Begin!
        print current_state
        print "Status: %s   Remaining_Guesses: %d" % (status, remaining_guesses)
        guess_alphabet = generate_guess(current_state, letters_guessed)
        print "Guess Alphabet: %s" % guess_alphabet

        url_suffix = "&token=%s&guess=%s" % (token, guess_alphabet)
        api_result_dict = requests.get(URL+url_suffix).json()
        letters_guessed.append(guess_alphabet)
        status, current_state, remaining_guesses = api_result_dict['status'], api_result_dict['state'], \
                                                   api_result_dict['remaining_guesses']

    print current_state
    if status == "FREE":
        print "FREE !!!!!! :))"
        return True
    else:
        print "DEAD :(("
        return False


if __name__ == "__main__":
    print "Year 2046. Welcome! Let's play Hangman."
    free_count, dead_count = 0, 0
    while True:
        print "\n\n******* Starting new game ********"
        result = play_hangman()
        if result:
            free_count += 1
        else:
            dead_count += 1
        print "Free Count: %d, Dead Count: %d" % (free_count, dead_count)
        #time.sleep(5)




