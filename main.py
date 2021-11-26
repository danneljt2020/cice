# funciones lambda
from mailbox import mbox

hola = lambda name: f"Hola {name}"
# print(hola("dannel"))

# ejemplo 2

calculator = {
    "add": lambda a, b: a + b,
    "square": lambda a: a * a,
    "cube": lambda a: a ** 3
}

values = [1, 2, 3, 4, 5]
result = list(filter(lambda value: value % 2 == 0, values))  # devuleve los pares

# print("Result pares", result)

# map
squares = map(lambda v: v ** 2, values)
# print(list(squares))

# print("CUBE", calculator['cube'](2))
# print("SQUARE", calculator['square'](2))

name_list = ["marcelo", "Pedro"]

names_start = list(filter(lambda name: name.lower().startswith("m"), name_list))
# print(list(names_start))

a_1 = [1, 2, 3, 4, 5, 7]
b_1 = [1, 2, 3, 4, 5, 6]

result_product_a_b = list(map(lambda a, b: a * b, a_1, b_1))
print(result_product_a_b)
