import sys, json

try:
    with open('day12.json') as f:
        data = json.load(f)
except:
    sys.exit("can't read day12.json")
    
taxes = 0

def json_iter(el):
    global taxes
    t = str(type(el))
    
    if 'dict' in t:         # object    -> dict
        print("- in dict")
        
        if 'red' in el.values():
            print("found red, skipping this dict")
        else:
            for key, child in el.iteritems():
                print("- child " + str(type(child)) + ": " + str(key))
                json_iter(child)
    elif 'list' in t:    # array     -> list
        print("- in list")
        for child in el:
            print("- child " + str(type(child)))
            json_iter(child)
    elif 'int' in t:
        print("- found int " + str(el))
        taxes += el
    else:
        print("- found " + t + ": " + str(el))
        
json_iter(data)

print("taxes = " + str(taxes))