import re

f = open('day12.json', 'r')

content = f.read()

#print(content)

m = re.findall('(-?\d+)', content)

print(sum(map(int, m)))