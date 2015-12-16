import sys

f = 'day16.input.txt'

try:
    lines = tuple(open(f, 'r'))
except:
    sys.exit("can't open %s" % f)
    
aunt_props = set([
        'children: 3',
        'cats: 7',
        'samoyeds: 2',
        'pomeranians: 3',
        'akitas: 0',
        'vizslas: 0',
        'goldfish: 5',
        'trees: 3',
        'cars: 2',
        'perfumes: 1'
    ])

for line in lines:
    aunt_set = set(line.strip().replace(':', ',', 1).split(', '))
    aunt_set_len = len(aunt_set) - 1    # substract name element
    
    aunt_inters = aunt_props & aunt_set
    
    if len(aunt_inters) == aunt_set_len:
        print(aunt_set)
        break
    
    