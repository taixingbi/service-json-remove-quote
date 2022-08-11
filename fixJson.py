import json

print("--------start--------")
name = "data"
with open(name + '.txt', 'r') as file:
    data = file.read().replace("\\", "")

dataJson = json.loads(data)
with open(name + '.json', 'w') as f:
    print(json.dumps(dataJson, indent=4, sort_keys=True))
    json.dump(dataJson, f, ensure_ascii=False, indent=4)

print("--------end--------")
