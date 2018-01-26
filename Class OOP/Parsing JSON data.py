import json
import m

my_string = '{"a": 1, "b": 2, "c": 3, "d": 4}'
data = json.loads(my_string)
for key in data:
    print(data[key])
print(data)
print(type(data))
json_string = json.dumps(data)
print(json_string)