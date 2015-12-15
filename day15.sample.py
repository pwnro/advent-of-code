import sys
from pprint import pprint
from operator import mul
from functools import reduce

#f = 'day15.input.txt'
f = 'day15.sample.txt'

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
    
#pprint(ingredients)

# necunoscutele: imi trebuie teaspoons de fiecare ingredient, suma lor este 100
teaspoons = [0] * len(ingredients)

results = []
# avem doar 2 valori de cantitati pentru teaspoons, x, y, x + y = 100, rescriem y -> y = x - 100, simplificam sistemul
# iteram prin toate valorile si calculam lista de t
for quant in range(100):
    # zero filled list de totaluri pe fiecare proprietate in functie de numarul de teaspoons
    t = [0] * (len(ingredients[0]) - 2)   # -2 pentru ca nu luam in calcul caloriile si numele din dict    
    
    ing1 = ingredients[0]
    ing2 = ingredients[1]
    
    t[0] = quant * (ing1['capacity'] - ing2['capacity']) + 100 * ing2['capacity']
    if t[0] < 1:
        continue
    
    t[1] = quant * (ing1['durability'] - ing2['durability']) + 100 * ing2['durability']
    if t[1] < 1:
        continue
    
    t[2] = quant * (ing1['flavor'] - ing2['flavor']) + 100 * ing2['flavor']
    if t[2] < 1:
        continue
    
    t[3] = quant * (ing1['texture'] - ing2['texture']) + 100 * ing2['texture']
    if t[3] < 1:
        continue
    
    results.append(t)
    
print(max(map(lambda x: reduce(mul, x), results)))