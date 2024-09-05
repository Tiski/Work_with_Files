# Задача: Создайте Python-скрипт, который:
#
# Сериализует сложный объект, содержащий вложенные словари и списки, в JSON-строку.
# Записывает полученную JSON-строку в файл output.json.
# Читает JSON-данные из файла output.json и десериализует их обратно в Python-объекты.
# 
# 
# Решение:
#
import json

# Сложная структура данных, содержащая вложенные словари и списки
data = {
    "company": "TechCorp",
    "employees": [
        {"name": "Mikhail", "role": "Engineer", "age": 30},
        {"name": "Tatyana", "role": "Manager", "age": 35},
        {"name": "Oksana", "role": "CTO", "age": 40}
    ],
    "location": {
        "city": "SBK",
        "state": "Bur",
        "zipcode": "671700"
    },
    "departments": ["Development", "Management", "HR"]
}


# Сериализация структуры данных в строку JSON
# Используем json.dumps() для преобразования Python-объекта в JSON-строку с форматированием (indent=4).
# Результат выводится на экран для проверки.
json_string = json.dumps(data, indent=4)
print(f"Сериализованный JSON:\nType: {type(json_string)}\n", json_string)  # Type: <class 'str'>  


# Запись JSON-строки в файл output.json
# Используем json.dump() для записи JSON-объекта в файл output.json.
# Файл создается или перезаписывается, если уже существует.
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)


print("\nJSON данные записаны в файл 'output.json'.")


# Чтение JSON-данных из файла и десериализация обратно в Python-объект
# Используем json.load() для чтения JSON-данных из файла и преобразования их обратно в Python-объект.
# Результат десериализации выводится на экран для проверки.
with open("output.json", "r") as file:
    loaded_data = json.load(file)


print(f"\nДесериализованные данные:\nType: {type(loaded_data)}\n", loaded_data)  # Type: <class 'dict'>
