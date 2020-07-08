import json
input='''
[
{
"id":"001",
"name":"satyam",
"x":"1"
},
{
"id":"002",
"name":"singh",
"x":"2"
}
]'''

info = json.loads(input)
print("User Counts", len(info))
for item in info:
    print(item["name"])
    print(item["x"])
    print(item["id"])
