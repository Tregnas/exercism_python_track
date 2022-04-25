def score(word):
    """
    Given a word, compute the Scrabble score for that word.

    LETTER VALUES:
    Letter                           Value
    A, E, I, O, U, L, N, R, S, T       1
    D, G                               2
    B, C, M, P                         3
    F, H, V, W, Y                      4
    K                                  5
    J, X                               8
    Q, Z                               10

    return: (int) score points
    """
    #I've used if... statement because python interpreter 3.9 was installed
    #For python 3.10 it's possible to solve with match...case statement
    
    score = 0
    for index in range(len(word)):
        if word.upper()[index] in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']:
            score += 1
        if word.upper()[index] in ['D', 'G']: 
            score += 2
        if word.upper()[index] in ['B', 'C', 'M', 'P']:
            score += 3
        if word.upper()[index] in ['F', 'H', 'V', 'W', 'Y']:
            score += 4
        if word.upper()[index] in ['K']:
            score += 5
        if word.upper()[index] in ['J', 'X']:
            score += 8
        if word.upper()[index] in ['Q', 'Z']:
            score += 10
    return score
