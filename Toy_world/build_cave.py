def build_cave(data):
    # TODO implement this function.
    try:
        # forming the basic 2D representation of cave
        cave = [[] for i in range(data['size'])]
        for i in cave:  # i = each_nested_list
            for j in range(data['size']):
                i.append('.')
        cave[data['entrance'][0]][data['entrance'][1]] = '@'
        cave[data['exit'][0]][data['exit'][1]] = 'X'
        if 'dragon' in data.keys() and len(data['dragon']) == 1:  # edited
            cave[data['dragon'][0]][data['dragon'][1]] = 'W'
        if 'sword' in data.keys() and len(data['sword']) == 1:  # edited
            cave[data['sword'][0]][data['sword'][1]] = 't'
        if 0 < len(data['treasure']) <= 3:
            for i in data['treasure']:  # i = each tuple in 'treasure' values
                cave[i[0]][i[1]] = '$'
        if 'walls' in data:
            for i in data['walls']:  # i = each tuple in the values of walls
                cave[i[0]][i[1]] = '#'
            
        return cave
    except:
        return 
    
        
