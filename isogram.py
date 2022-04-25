def is_isogram(string):
    """
    Determine if a word or phrase is an isogram.

    string: (str) string given to check
    returns: (boolean) is isogram or not
    """
    stripped_string = string.replace("-", "").replace(" ", "").lower()
    return len(set(stripped_string)) == len(stripped_string)
