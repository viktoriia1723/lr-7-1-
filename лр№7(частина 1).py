import random

def print_dictionary(dictionary):
    print("Словник учнів та їх зросту:")
    for name, height in dictionary.items():
        print(f"{name}: {height} см")

def add_student(dictionary, name, height):
    dictionary[name] = height
    print(f"Додано учня {name} зі зростом {height} см")

def remove_student(dictionary, name):
    if name in dictionary:
        del dictionary[name]
        print(f"Видалено учня {name}")
    else:
        print(f"Учня {name} не знайдено в словнику")

def print_sorted_dictionary(dictionary):
    print("Відсортований словник за прізвищами:")
    for name in sorted(dictionary.keys()):
        print(f"{name}: {dictionary[name]} см")

def find_students_shorter_than_new(dictionary, new_height):
    return [name for name, height in dictionary.items() if height < new_height]

def find_position_for_new_student(dictionary, new_height):
    sorted_heights = sorted(dictionary.values(), reverse=True)
    for i, height in enumerate(sorted_heights):
        if height < new_height:
            return list(dictionary.keys())[list(dictionary.values()).index(sorted_heights[i-1])]
    return None

def find_closest_height_student(dictionary, new_height):
    return min(dictionary, key=lambda x: abs(dictionary[x] - new_height))

# Ініціалізація словника
students = {
    "Іванов": 185,
    "Петров": 182,
    "Сидоров": 178,
    "Коваленко": 175,
    "Шевченко": 172,
    "Бондаренко": 170,
    "Мельник": 168,
    "Павленко": 165,
    "Ткаченко": 162,
    "Кравченко": 160
}

while True:
    print("\nМеню:")
    print("1. Вивести словник")
    print("2. Додати учня")
    print("3. Видалити учня")
    print("4. Вивести відсортований словник")
    print("5. Обробити дані нового учня")
    print("6. Вийти")

    choice = input("Виберіть опцію: ")

    if choice == '1':
        print_dictionary(students)
    elif choice == '2':
        name = input("Введіть прізвище учня: ")
        height = int(input("Введіть зріст учня (см): "))
        add_student(students, name, height)
    elif choice == '3':
        name = input("Введіть прізвище учня для видалення: ")
        remove_student(students, name)
    elif choice == '4':
        print_sorted_dictionary(students)
    elif choice == '5':
        new_height = int(input("Введіть зріст нового учня (см): "))
        shorter_students = find_students_shorter_than_new(students, new_height)
        print("a) Учні, зріст яких менше нового учня:")
        print(", ".join(shorter_students))
        
        position = find_position_for_new_student(students, new_height)
        print(f"б) Новий учень повинен бути записаний після учня: {position}")
        
        closest = find_closest_height_student(students, new_height)
        print(f"в) Учень з найближчим зростом: {closest}")
    elif choice == '6':
        print("До побачення!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")