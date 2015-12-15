import sys
from operator import mul
from functools import reduce

f = 'day15.input.txt'
#f = 'day15.sample.txt'

try:
    lines = tuple(open(f, 'r'))
except:
    sys.exit("can't open %s" % f)
    
# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8

ingredients = []
for line in lines:
    words = line.replace(',', '').split()
    ingredients.append({
        'name': words[0],
        'capacity': int(words[2]),
        'durability': int(words[4]),
        'flavor': int(words[6]),
        'texture': int(words[8]),
        'calories': int(words[10])
    })

part1 = []
part2 = []
# avem doar 2 valori de cantitati pentru teaspoons, x, y, x + y = 100, rescriem y -> y = x - 100, simplificam sistemul
# iteram prin toate valorile si calculam lista de t

for x in range(100):
    for y in range(100):
        for z in range(100):
            v = 100 - (x + y + z)
            
            # valorile de cantitati teaspoons pentru fiecare ingredient
            if v + x + y + z > 100:
                continue
            
            t = [0] * 4
            
            skip = False
            for idx, prop in enumerate(['capacity', 'durability', 'flavor', 'texture']):
                t[idx] = v * ingredients[0][prop] + x * ingredients[1][prop] + y * ingredients[2][prop] + z * ingredients[3][prop]
                if t[idx] < 1:
                    skip = True

            if skip == True:
                continue
                    
            score = reduce(mul, t)
            
            part1.append(score)
                    
            # aceasta reteta trebuie sa aiba un numar de calorii de 500
            prop = 'calories'
            cals = v * ingredients[0][prop] + x * ingredients[1][prop] + y * ingredients[2][prop] + z * ingredients[3][prop]
            
            if cals == 500:    
                part2.append(reduce(mul, t))
            
print('part1: %d' % max(part1))
print('part2: %d' % max(part2))
