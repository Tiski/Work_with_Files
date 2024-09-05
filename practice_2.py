# Задача: Определите класс Employee с атрибутами name, role, и age. Создайте список объектов этого класса. 
# 
# Напишите код для:
#
# Сериализации списка объектов класса Employee в JSON-формат.
# Записи JSON-данных в файл employees.json.
# Десериализации данных из файла обратно в объекты класса Employee.
#
#
# Решение:
#
import json

# Определение класса Employee
class Employee:
    def __init__(self, name: str, role: str, age: int):
        self.name = name
        self.role = role
        self.age = age


# Создание списка объектов класса Employee
employees = [
    Employee("Mikhail", "Engineer", 30),
    Employee("Tatyana", "Manager", 35),
    Employee("Oksana", "CTO", 40)
]

# Функция для сериализации объектов Employee в JSON
def employee_to_dict(emp):
    return {"name": emp.name, "role": emp.role, "age": emp.age}


# Сериализация списка объектов Employee в JSON-строку
json_string = json.dumps([employee_to_dict(emp) for emp in employees], indent=4)
print("Сериализованный JSON:\n", json_string)


# Запись JSON-строки в файл employees.json
with open("employees.json", "w") as file:
    json.dump([employee_to_dict(emp) for emp in employees], file, indent=4)


print("\nJSON данные записаны в файл 'employees.json'.")


# Чтение JSON-данных из файла и десериализация обратно в объекты класса Employee
with open("employees.json", "r") as file:
    loaded_employees = json.load(file)


# Преобразование JSON обратно в объекты Employee
deserialized_employees = [Employee(**emp) for emp in loaded_employees]
for emp in deserialized_employees:
    print(f"\nДесериализованный объект: Name: {emp.name}, Role: {emp.role}, Age: {emp.age}")
