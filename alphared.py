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


def reduce_alphabet(seq, alphabet_size = 7, unknown_symbol='X'):
    """
    Reduces a protein sequence to a smaller alphabet.

    Args:
        seq (str): Original protein sequence.
        reduction_map (dict): Mapping from amino acids to reduced symbols.
        unknown_symbol (str): Symbol to use for unknown residues.

    Returns:
        str: Reduced sequence.
    """
    if alphabet_size == 7:
        reduction_map = scheme7_map
    elif alphabet_size == 10:
        reduction_map = scheme10_map
    else:
        raise ValueError("Unsupported alphabet size. Use 7 or 10.")
    reduced_seq = ''.join([reduction_map.get(aa, unknown_symbol) for aa in seq])
    return reduced_seq
