import sys
from math import ceil

#f = 'day14.input.txt'
f = 'day14.sample.txt'

try:
    lines = tuple(open(f, 'r'))
except:
    sys.exit("can't open %s" % f)
    
reindeers = []
for line in lines:
    words = line.strip().split()
    reindeers.append({
        'name': words[0],
        'speed': int(words[3]),     # km/s
        'burst': int(words[6]),     # s
        'rest': int(words[-2])      # s
    })

race_len = 1100

distances = []
for reindeer in reindeers:    
    burst = reindeer['burst']
    speed = reindeer['speed']
    rest = reindeer['rest']

    # durata unui hop in secunde
    hop_s = burst + rest
    
    # distanta parcursa per hop, d = t x v
    hop_d = burst * speed
    
    # numarul de hopuri (rotunjit superior)
    hops = ceil(race_len / hop_s)
    
    # distanta parcursa, d = hop_d * hops
    distance = hop_d * hops
    distances.append(distance)
    print("%s termina in %d hopuri, parcurgand distanta %d" % (reindeer['name'], hops, distance))

print("max = %d" % max(distances))