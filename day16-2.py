import sys

f = 'day16.input.txt'

try:
    lines = tuple(open(f, 'r'))
except:
    sys.exit("can't open %s" % f)
    
check = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

for line in lines:
    auntie_list = line.strip().replace(':', ',', 1).replace('Sue', 'Sue:').split(', ')
    
    auntie = {}
    
    # create auntie dictionary
    for el in auntie_list:
        k, v = el.split(': ')
        v = int(v)
        
        auntie[k] = v
        
    if 'cats' in auntie:
        if auntie['cats'] < check['cats']:
            continue
    
    if 'trees' in auntie:
        if auntie['trees'] < check['trees']:
            continue    
        
    if 'pomeranians' in auntie:
        if auntie['pomeranians'] > check['pomeranians']:
            continue
    
    if 'goldfish' in auntie:
        if auntie['goldfish'] > check['goldfish']:
            continue        
    
    auntie_copy = auntie.copy()
    check_copy = check.copy()
    for k in ['Sue', 'cats', 'trees', 'pomeranians', 'goldfish']:
        try:
            del auntie_copy[k]
        except:
            pass
        
        try:
            del check_copy[k]
        except:
            pass

    auntie_set = set([k + ': ' + str(auntie_copy[k]) for k in auntie_copy.keys()])
    check_set = set([k + ': ' + str(check_copy[k]) for k in check_copy.keys()])
    
    intersection = auntie_set & check_set
    
    if len(intersection) == len(auntie_set):
        print(auntie)
        sys.exit()
        


    