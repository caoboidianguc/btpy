import json



data = {}
data['name'] = 'Quang'
data['phone'] = 8033399070
data['address'] = {}
data['address']['road'] = "Newgate End"
data['address']['city'] = 'Columbia'
data['address']['state'] = "SC"
data['national'] = []
data['langauge'] = {}
data['langauge']['native'] = "Vietnamese"
data['langauge']['foreign'] = "English"

#serialize
serialize = json.dumps(data, indent=4)
print(serialize)

print("\n\n\n\n")

#deserialize
try:
    deserialize = json.loads(serialize)
    print(deserialize)
except json.JSONDecodeError as e:
    print("loi tu serialize", e)