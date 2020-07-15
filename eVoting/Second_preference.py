def second_preference(votes):
    # TODO implement this function.
    frequency = {}
    for i in votes:
        if i[0] in frequency:
            frequency[i[0]] += 1
        else:
            frequency[i[0]] = 1 
    deck = []
    for j in sorted(frequency):
        if frequency[j] == max(frequency.values()) or frequency[j] != min(frequency.values()):
            deck.append(j)  #min er key baade shob dhuklo deck a
    if not max(frequency.values()) > 0.5 * len(votes):            
        for k in range(len(votes)):            
            if min(frequency.keys()) in votes[k][0] and votes[k][1] in deck:  
                frequency[votes[k][1]] += 1
        highest_vote=[]
        for voter in sorted(frequency):  #newly sorted after gettin 2nd set vote
            if frequency[voter] == max(frequency.values()):
                highest_vote.append(voter)
        if len(highest_vote) > 1:
            return 'tie'
        else:
            return max(frequency, key=frequency.get)
    else:
        return max(frequency, key=frequency.get)
