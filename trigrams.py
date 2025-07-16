from collections import Counter
import itertools

AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"
TRIGRAMS = [''.join(p) for p in itertools.product(AMINO_ACIDS, repeat=3)]
trigram_to_idx = {tri: idx for idx, tri in enumerate(TRIGRAMS)}

def get_bag_of_trigrams(seq):
    counts = [0]*len(TRIGRAMS)
    for i in range(len(seq)-2):
        tri = seq[i:i+3]
        if tri in trigram_to_idx:
            counts[trigram_to_idx[tri]] += 1
    return counts


# Scheme 1: Alphabet Size 7
scheme7_map = {
    'E': '1', 'K': '1', 'Q': '1', 'R': '1',
    'F': '2', 'I': '2', 'V': '2',
    'L': '3', 'M': '3', 'W': '3', 'Y': '3',
    'A': '4', 'C': '4', 'H': '4',
    'S': '5', 'T': '5',
    'D': '6', 'N': '6',
    'G': '7', 'P': '7'
}

# Scheme 2: Alphabet Size 10
scheme10_map = {
    'E': '1', 'K': '1', 'Q': '1', 'R': '1',
    'I': '2', 'V': '2',
    'L': '3', 'Y': '3',
    'F': '4',
    'A': '5', 'M': '5',
    'W': '6',
    'H': '7', 'T': '7',
    'C': '8',
    'D': '9', 'N': '9', 'S': '9',
    'G': '10', 'P': '10'
}


def generate_trigram_vocab(alphabet):
    """
    Generates a list of all possible trigrams from the given alphabet symbols.
    """
    trigrams = [''.join(p) for p in itertools.product(alphabet, repeat=3)]
    return trigrams

import numpy as np

def get_bag_of_trigrams_reduced( seq, alphabet_size):
    """
    Returns a function that maps a sequence to its bag-of-trigrams feature vector
    using the reduced alphabet mapping and vocabulary.
    """
    if alphabet_size == 7:
        reduction_mapping = scheme7_map
    elif alphabet_size == 10:
        reduction_mapping = scheme10_map
    else:
        raise ValueError("Unsupported alphabet size. Use 7 or 10.")
    
    # Generate reduced alphabet symbols
    reduced_alphabet = sorted(set(reduction_mapping.values()))
    
    # Generate all possible trigrams
    vocab = generate_trigram_vocab(reduced_alphabet)
    trigram_to_index = {tri: idx for idx, tri in enumerate(vocab)}
    
    # Initialize feature vector
    features = np.zeros(len(vocab))
    
    # Slide window over reduced sequence
    for i in range(len(seq) - 2):
        tri = seq[i:i+3]
        if tri in trigram_to_index:
            features[trigram_to_index[tri]] += 1
    
    return features

