import os
import json

file_path = "/mnt/sda/juyoung/CLICK/Dataset/Culture/Korean History/History_KHB_new.json"

with open(file_path, "r", encoding="utf-8") as file:
    data_list = json.load(file)
    
# print(data_list)
print(len(data_list))

ids = []
for data in data_list:
    ids.append(data['id'])

assert(len(ids) == len(data_list))
assert(len(ids) == len(set(ids)))