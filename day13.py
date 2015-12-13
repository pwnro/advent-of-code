import itertools as it
import sys

try:
    lines = tuple(open('day13.input.txt', 'r'))
except:
    sys.exit("can't open day13.input.txt")
    
matrix = {}
for line in lines:
    words = line.strip().split()
    p1, op, p2, val = words[0], words[2], words[-1].strip('.'), int(words[3])
    
    if op != 'gain':
        val = 0 - val
    
    if p1 not in matrix:
        matrix[p1] = {'me': 0}
        
    matrix[p1][p2] = val

ppl = matrix.keys()
matrix['me'] = {person: 0 for person in ppl}
ppl.append('me')

# let the overkill commence
perms = it.permutations(ppl)

happy_list = []
for perm in perms:
    happy = 0
    for p1, p2 in zip(perm, perm[1 : ] + perm[ : 1]):
        happy += matrix[p1][p2]
        happy += matrix[p2][p1]
        
    happy_list.append(happy)

print(max(happy_list))