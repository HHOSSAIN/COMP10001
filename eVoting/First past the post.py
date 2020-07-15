Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def first_past_the_post(votes):
    # TODO implement this function.
    frequency = {}
    for voter in votes:
        if voter in frequency:
            frequency[voter] += 1  #key=frequency.get
        else:
            frequency[voter] = 1
    deck = []        
    for voter in sorted(frequency): #list of the names in alpahbetical order
        if frequency[voter] == max(frequency.values()): 
            deck.append(voter)
    if len(deck) > 1:
        return "tie"
    else:
        return max(frequency, key = frequency.get)  # or max(frequency)
