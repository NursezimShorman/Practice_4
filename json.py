#1
import json

x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["age"])
#2
import json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)

print(y)
