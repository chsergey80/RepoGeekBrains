import json

# params = {'зарплата': 50000, 'bonus': 20000}
params = [145, 67, 587]

#params_as_str = json.dumps(params, ensure_ascii=False, indent=4)
print(type(params), params)
#print(type(params_as_str), params_as_str)

with open('params.json', 'w', encoding='utf-8') as f:
    #f.write(params_as_str)
    json.dump(params, f)

with open('params.json', 'r', encoding='utf-8') as f:
    #params_as_str = f.read()
    params = json.load(f)

#params = json.loads(params_as_str)
print(type(params), params)

