import sys
import itertools as it

f = 'day17.input.txt'

total_liters = 150

try:
    lines = tuple(open(f, 'r'))
except:
    sys.exit("can't open %s" % f)

part1 = []

containers = list(map(int, lines))

for i in range(len(lines)):
    combs = it.combinations(containers, i)
    #combs = list(combs)
    
    for comb in combs:
        if sum(comb) == total_liters:
            part1.append(comb)  
            
print(len(part1))

min_cont = 0
for comb in part1:
    nr_cont = len(comb)
    
    if min_cont == 0:
        min_cont = nr_cont
        
    min_cont = min(min_cont, nr_cont)

part2 = [c for c in part1 if len(c) == min_cont]

print(len(part2))


