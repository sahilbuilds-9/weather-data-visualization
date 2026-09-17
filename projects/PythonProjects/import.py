# Date and time
import datetime
today = datetime.date.today()
print(today)  # 2024-01-15

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)

# ///////////////////

data = {
    "Name": ["Rahul", "Priya", "Aman"],
    "Marks": [85, 90, 78]
}

students = list(zip(data["Name"], data["Marks"]))

print("Name  Marks")
for name, marks in students:
    print(f"{name:<6}{marks}")