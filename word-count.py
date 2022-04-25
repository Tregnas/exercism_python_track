import re

def count_words(sentence):
    """ Given a phrase, count the occurrences of each word in that phrase.
    
    sentence: (str) given phrase
    return: (dict) each word in phrase: word occurence
    """
    
    stripped = re.sub(r"\'*[\s.!?,&@$%^&:_]+\'*|\'{2,}|^\'|\'$", " ", sentence.lower())
    as_list = stripped.split()

    unique = {}
    for word in as_list:
        if word in unique:
            unique[word] += 1
        else:
            unique[word] = 1
    return unique
