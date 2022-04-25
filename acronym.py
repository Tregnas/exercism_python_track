import re

def abbreviate(words):
    """
    Convert a phrase to its acronym.

    words: (str) given titled string
    return: (str) abbreviated string
    """
    acronym = ""
    stripped = re.sub(r"\'*[\s.!?,&@$%^&:_-]+\'*|\'{2,}|^\'|\'$", " ", words).split()
    for word in stripped:
        acronym += word[0].upper()
    return acronym
