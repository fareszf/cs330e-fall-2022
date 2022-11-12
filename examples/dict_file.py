import json
# Dictionary
person = { "name": "John Smith", 
           "age": 35, 
           "address": {"street": "5 main St.", "city": "Austin"}, 
           "children": ["Mary", "Abel"], 
           "has_car": None }

# Converting the Dictionary into a JSON file
with open('person_to_json.json', 'w') as fp:
    json.dump(person, fp, indent=4)
    
js = json.dumps(person)   
assert js ==  '{"name": "John Smith", \
"age": 35, \
"address": {"street": "5 main St.", "city": "Austin"}, \
"children": ["Mary", "Abel"], \
"has_car": null}'
                
       
# Converting the JSON file "person_to_json.json" into a Dictionary
def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
    return jsn
    
person = load_json('person_to_json.json')

assert person["age"]               == 35
assert person["address"]["street"] == "5 main St."
assert person["address"]["city"]   == "Austin"
assert person["children"][0]       == "Mary"
assert person["children"][1]       == "Abel"
assert person["has_car"]           == None
