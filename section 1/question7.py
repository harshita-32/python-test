Employees = [
    "id: 101, name: harshita",
    "id: 102, name: jai",
    "id: 103, name: jaya"
]

with open('employees.txt', 'w') as file:
    file.writelines(Employees)
print("File created successfully")

print("\nReading employee file")
with open('employees.txt', 'r') as file:
    print(file.read())