def is_valid_vote(vote, candidates):
    # TODO implement this function.
    z = set(vote)
    for i in range(len(z)):
        if len(z) == len(candidates) and len(vote) == len(candidates) and \
        vote[i] in candidates:
            return True
        else:
            return False
  
