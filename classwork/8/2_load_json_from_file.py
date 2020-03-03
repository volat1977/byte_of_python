import json

with open("test.json") as f:
    content = f.read()

    result = json.loads(content)

    print(result)

    print(result['inner']['inner_prop1'])
