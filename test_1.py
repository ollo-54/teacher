import json
import data

print(data.goals, '\n', data.teachers)
#data1{} = data
#print(data1)
#my_list = ['foo', 'bar']
contents = json.dumps(data.teachers)
with open("data.json", "w", encoding='utf-8') as f:
    f.write(contents)

#with open('data.py', "w", encoding="utf-8") as file:
#    json.dump(file, 'data.json')


#with open('data.json', 'r', encoding='utf8') as data_file:
#    data = json.load(data_file)
#    print(data_file)

#with open('data.json', 'r') as data_file:
#    profiles = json.load(data_file.read())
#print(profiles[id])
