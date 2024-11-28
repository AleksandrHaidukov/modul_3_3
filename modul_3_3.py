# Задание 1. Функция с параметрами по умолчанию:
print("Задание 1")
print(" ")
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b=25)
print_params(c=[1,2,3])
print(" ")


# Задание 2. Распаковка параметров:
print("Задание 2")
print(" ")
values_list = [45, "String", [1,2,3]]
values_dict = {"a": 3, "b": "new_string", "c": False}
print_params(*values_list)
print_params(**values_dict)
print(" ")

# Задание 3. Распаковка + отдельные параметрыЖ
print("Задание 3")
print(" ")
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)