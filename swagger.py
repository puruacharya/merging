import json

with open('swagger.json', 'r') as file:
    data = json.load(file)
paths = data.get('paths')

print("Paths:")
for path, methods in paths.items():
    print(path)
