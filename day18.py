import sys

# compute for part 2
part2 = True

f = 'day18.input.txt'
#f = 'day18.sample.txt'

matrix_size = 100
#matrix_size = 6

#steps = 5
steps = 100

padded_matrix_size = matrix_size + 2
matrix = []

try:
    lines = tuple(open(f, 'r'))
except:
    sys.exit("can't open %s" % f)

for idx, line in enumerate(lines):
    matrix.append(list(line.strip()))

# pad matrix with neighbours    
def pad_matrix(matrix, pad = 'o'):
    global matrix_size, padded_matrix_size
    padded_matrix = []
    
    for i in range(padded_matrix_size):
        row = []
        for j in range(padded_matrix_size):
            if i > 0 and i < padded_matrix_size -1 and j > 0 and j < padded_matrix_size -1:
                row.append(matrix[i-1][j-1])
            else:
                row.append(pad)
        padded_matrix.append(row)
    return padded_matrix

def next_state(matrix):
    global matrix_size, padded_matrix_size
    
    # compute next state for part2 -> corner lights always on
    if part2:
        matrix[0][0] = 'p2'
        matrix[0][matrix_size-1] = 'p2'
        matrix[matrix_size-1][matrix_size-1] = 'p2'
        matrix[matrix_size-1][0] = 'p2'
        
    matrix_padded = pad_matrix(matrix)
    matrix_new = matrix.copy()
    
    for i in range(padded_matrix_size):
        for j in range(padded_matrix_size):
            c = matrix_padded[i][j]
            
            if c == 'o':
                continue
            else:
                # get neighbours
                neighbours_upstairs = matrix_padded[i-1][j-1:(3+j-1)]
                neighbours_downstairs = matrix_padded[i+1][j-1:(3+j-1)]
                
                neighbours_same_floor = matrix_padded[i][j-1:(3+j-1)]        
                # remove the actual light we're on
                del neighbours_same_floor[1]
                
                neighbours = neighbours_upstairs + neighbours_downstairs + neighbours_same_floor
                
                if part2:
                    neighbours_lit = neighbours.count('#') + neighbours.count('p2')
                else:
                    neighbours_lit = neighbours.count('#')
                
                # A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
                if c == '#':
                    if neighbours_lit in [2, 3]:
                        # keep light on
                        pass
                    else:
                        # turn light off
                        matrix_new[i-1][j-1] = '.'
                # A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.                        
                else:
                    if neighbours_lit == 3:
                        # turn light on
                        matrix_new[i-1][j-1] = '#'
                    else:
                        # keep light off
                        pass
    return matrix_new

for step in range(steps):
    matrix = next_state(matrix)

lights_on = 0
for i in range(matrix_size):
    for j in range(matrix_size):
        if matrix[i][j] == '#' or (part2 and matrix[i][j] == 'p2'):
            lights_on += 1
            
print(lights_on)

