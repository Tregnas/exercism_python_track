def distance(strand_a, strand_b):
    """Calculate the Hamming distance between two strings.
 
	strand_a (str): the first string.
	strand_b (str): the second string.
 
	returns: (int) the hamming distance.
	"""
    
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    mistakes = 0
    for index in range(len(strand_a)):
        if strand_a[index] != strand_b[index]:
            mistakes +=1
    return mistakes
