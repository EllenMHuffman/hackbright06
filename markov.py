"""Generate Markov text from text files."""

from sys import argv
from random import choice
from random import sample


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as f:
        text = f.read()

    return text

# text_string = open_and_read_file('green-eggs.txt')
# print make_chains(text_string)

def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()
    words.append(None)
    for i in range(len(words) - n):
        markov_key = tuple(words[i:i+n])
        # print markov_key
        # import pdb; pdb.set_trace()
      
        if chains.get(markov_key):
            # chains[markov_key] = chains[markov_key] + [words[i+2]]
            chains[markov_key].append(words[i+n])
        else:
            chains[markov_key] = [words[i+n]]
            # print chains
    
    # import pdb; pdb.set_trace()

    return chains


def make_text(chains, n):
    """Return text from chains."""


    first_ngram = choice(chains.keys())
    # print first_ngram
    words = list(first_ngram)

    while True:

        # allows you to go one loop at a time to debug, n for next line
        # import pdb; pdb.set_trace()

        next_word = choice(chains[first_ngram])
        # print next_word

        if next_word is None:
            break

        words.append(next_word)

        first_ngram_list = list(first_ngram)
        # print first_ngram_list
        ngram_list = first_ngram_list[-(n-1):] 
        ngram_list.append(next_word)
        # print ngram_list
        first_ngram = tuple(ngram_list)
        # print first_ngram

    return " ".join(words)


input_path = argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, int(argv[2]))

# Produce random text
random_text = make_text(chains, int(argv[2]))

print random_text
