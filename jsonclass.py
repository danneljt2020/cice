import json

json_file = open('data.json', )

data = json.load(json_file)

print(data['person'])

