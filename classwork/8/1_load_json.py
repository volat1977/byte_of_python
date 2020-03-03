import json

result = json.loads('{"test1": 1, "test2": 2}')
print(result)
print(result['test1'])
print(type(result))

