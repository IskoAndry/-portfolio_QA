import json


with open("date.json", "r") as f:
    date = json.load(f)

number_of_objects = len(date)

print(f"Количество объектов: {number_of_objects}")
