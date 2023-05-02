def findall(guess, word):
    '''Yields all the positions of
    the pattern `guess` in the string `word`.'''
    i = word.find(guess)
    while i != -1:
        yield i
        i = word.find(guess, i+1)