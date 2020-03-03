import json

with open("test.json") as f:
        content = f.read()
        result = json.loads(content)

        result["array"] = 123123

        with open("result.json", mode="w") as f2:
            json_content = json.dumps(result)

            f2.write(json_content)


