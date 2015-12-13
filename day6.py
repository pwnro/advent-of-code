from numpy import array, zeros, logical_not, count_nonzero

maxCols = 1000
maxRows = 1000

# cream matricea de becuri
becuri = zeros([maxCols, maxRows], bool)

for l in open('day6.input.txt'):
    [op, p1, pula, p2] = l.replace('turn ', '').split()
    
    [x1, y1] = map(int, p1.split(','))
    [x2, y2] = map(int, p2.split(','))
    
    rows = array(range(y1, y2+1), int)
    cols = array(range(x1, x2+1), int)
    
    if op == 'on':
        becuri[rows[:, None], cols] = True
    elif op == 'off':
        becuri[rows[:, None], cols] = False
    else:
        jmkerie = becuri[rows[:, None], cols]
        becuri[rows[:, None], cols] = logical_not(jmkerie)
    
print count_nonzero(becuri)