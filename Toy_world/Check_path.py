import math 
def check_path(data, path):
    # TODO implement this function.
    rows = data["size"]
    columns  = data["size"]
    ''' 'EW'= change in column,i.e change in position inside same sublist. 
    'NS'= change in row,i.e change in sublist. '''
    movements = {'S': 1, 'N': -1, 'E': 1, 'W': -1}
    start = list(data['entrance'])
    route=[data['entrance']]  # list of path coordinates
    # making a list of the path using the "coordinates" they pass through
    for i in path:
        if i in 'NS':
            start[0] += movements[i]  # row
            route.append(tuple(start))
        if i in 'EW':
            start[1] += movements[i]
            route.append(tuple(start))
    # checking whether a 'W' is present, creating problems in the taken path
    if 'dragon' in data: 
        d_position = data['dragon']
        s_position = data['sword']    
        for i in range(len(route)):
            if route[i] == d_position:  # confirming if dragon in route steps
                d_position = i
            if route[i] == s_position:  # confirming if sword in route steps
                s_position = i 
        ''' checking if Falca gets to any of the eight locations 
        adjacent to a dragon without a sword '''
        if type(d_position) == int and type(s_position) == int:
            for i in route:   # checking for each step in route
                if d_position < s_position:
                    distance = math.sqrt((i[0] - data['dragon'][0] ** 2) + 
                                    (i[1] - data['dragon'][1]) ** 2)
                    if distance in (1, math.sqrt(2)):
                        return False
        # checking if passing through dragon before collecting sword
        if type(d_position) == int and type(s_position) == int:
            if d_position < s_position:
                return False
    # checking if the taken path had any walls in it
    if 'walls' in data:
        for i in data['walls']:
            if i in route:
                return False
    # checking if all the treasures were collected
    treasure_count = []
    z = len(data['treasure'])
    for i in data['treasure']:
        if i in route:
            treasure_count.append(i)       
    if len(treasure_count) != z:
        return False
    # checking if any step in route was outside of cave
    for i in route:  
        if not (i[0]>=0 and i[1]>=0 and i[0]< rows and i[1] < columns):
                return False
    exit_pos = data['exit']
    if route[-1] != exit_pos:
        return False
    return True
