Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def multiple_preference(votes):
    # TODO implement this function.
    frequency = {}
    for i in votes:
        if i[0] in frequency:
            frequency[i[0]] += 1
        else:
            frequency[i[0]] = 1    
    deck = [] 
    for j in sorted(frequency):
        if frequency[j] == max(frequency.values()) or frequency[j] != \
        min(frequency.values()):
            deck.append(j) 
    if not max(frequency.values()) > 0.5 * len(votes):
        min_deck = [] 
        for key in frequency:
            if frequency[key] == min(frequency.values()):
                min_deck.append(key)  #getting a list of keys with min values
        for i in range(len(votes)):   
            if sorted(min_deck)[0] in votes[i][0]:         
                if not votes[i][1] in frequency:
                    for l in range(2, len(votes[0])):
                        if votes[i][l] in frequency: 
                            frequency[votes[i][l]] += 1 
                            del frequency[votes[i][0]]
                            for h in range(len(votes)):
                                if sorted(min_deck)[0] in votes[h] and \
                                len(min_deck) > 1:
                                    votes[h].remove(sorted(min_deck)[0])
                            break                      
                else:    
                    frequency[votes[i][1]] += 1 
                    del frequency[votes[i][0]]
                    for h in range(len(votes)):
                        if sorted(min_deck)[0] in votes[h]:
                            votes[h].remove(sorted(min_deck)[0])
                if not max(frequency.values()) > 0.5 * (len(votes)): 
                    if len(min_deck) > 1:
                        z=set(sorted(min_deck).pop(0))
                        y=set(min_deck)
                        min_deck = list(y - z) 
                        if votes[i][0] in min_deck: 
                            min_deck.remove(votes[i][0])                                                    
        highest_vote=[]
        for voter in sorted(frequency):
            if frequency[voter] == max(frequency.values()):
                highest_vote.append(voter)
        if len(highest_vote) > 1:
            return 'tie'   
        else:
            return max(frequency, key=frequency.get)                  
    else:
	return max(frequency, key=frequency.get) 
