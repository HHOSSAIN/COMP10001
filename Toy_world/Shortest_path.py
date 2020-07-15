import math
def shortest_path(data, start, end, has_sword):
    # TODO implement this function.
        # node = start(initially), symbols:'W'=dragon, 't'=sword
        unexplored = [start]  # my queue
        explored =  set()
        steps = 0
        rows = data["size"]
        columns  = data["size"]
        if unexplored == []:
            return None
        if start == end:
            return steps
        while unexplored:
            new_coordinates=[]
            for i in unexplored: 
                explored.add(i)
                # probable next moves from a point
                a = i[0] + 1  # a=dx, (south), (row change)
                b = i[0] - 1  # b=dx, (north), (row change)
                c = i[1] + 1  # c=dy, (east), (column change)
                d = i[1] - 1  # d=dy, (west), (column change)
                coordinates = [(i[0], c), (i[0], d), (a, i[1]), (b, i[1])]
                ''' if 't' taken, path is same to path in absence of 'W', i.e.
                the path is unaffected by presence or absence of 'W' if 
                carrying 't'('t' = sword, 'W' = dragon). '''
                if 'dragon' not in data or has_sword:
                    for j in coordinates:
                        if (j[0]>=0 and j[1]>=0 and j[0]< rows and 
                            j[1] < columns):
                            if 'walls' in data and j not in data['walls']:  
                                if j not in unexplored and j not in explored:
                                    if j not in new_coordinates:
                                        new_coordinates.append(j) 
                            elif 'walls' not in data:
                                if j not in unexplored and j not in explored:  
                                    if j not in new_coordinates:
                                        new_coordinates.append(j)                                 
                if 'dragon' in data:
                    if not has_sword:  # not carrying a sword 
                        # ensuring move is inside cave    
                        for j in coordinates:  # j=next move
                            if (j[0] >= 0 and j[1]>=0 and j[0]<rows and
                            j[1]< columns):
                                if j not in new_coordinates:
                                    new_coordinates.append(j)
                                    distance = (math.sqrt((j[0] -
                                    data['dragon'][0])** 2 +(j[1] -
                                    data['dragon'][1]) ** 2))        
                                # ensuring move not in 8 adjacent blocks to 'W'
                                    if distance in (1, math.sqrt(2)):
                                        new_coordinates.remove(j)
                        # ensuring moves aren't repeated or in wall positions
                        for k in new_coordinates:
                            if 'walls' in data and k not in data['walls'] \
                                and k not in unexplored and k not in explored:
                                True 
                            elif 'walls' not in data:
                                if k not in unexplored and k not in explored:  
                                    True
                            else:
                                new_coordinates.remove(k)
                        for l in new_coordinates:
                            if l in explored or l in unexplored: 
                                if 'walls' in data and l in data['walls']:  
                                    new_coordinates.remove(l) 
                                elif 'walls' not in data:
                                    if l in explored or l in unexplored: 
                                        new_coordinates.remove(l)
            # changing queue to its child nodes after iteration of 1 level done
            unexplored = new_coordinates
            if unexplored == []:
                return None
            if end not in unexplored:
                steps += 1 
            else:
                steps += 1
                return steps
