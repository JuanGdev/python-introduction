### List ###
#   Una lista es como un arreglo pero con operaciones más completas sobre estas estructuras de datos
my_list = list()
my_other_list = [32, 12, 2, 5, 6, 7]

my_list = [23, 12, "Test"]

print(my_list)
print(my_other_list[1])
print(my_other_list[-1])    #   Starts from last index

"""
En Python, una tupla es una estructura de datos inmutable y ordenada que puede contener elementos de diferentes tipos. 
Se utiliza para almacenar una colección de elementos relacionados. A diferencia de las listas, las tuplas no se pueden 
modificar una vez que se crean, lo que significa que son inmutables.

Las tuplas se definen mediante paréntesis (), separando los elementos con comas. Por ejemplo:
"""

mi_tupla = (1, 2, 3, 'a', 'b', 'c')

"""
    Además de la indexación, también puedes utilizar la asignación múltiple para extraer los elementos de una tupla en
    variables individuales. Por ejemplo:
"""
mi_tupla_dos = (1,2,3)
x, y, z = mi_tupla_dos
print(x)  # Imprime 1
print(y)  # Imprime 2
print(z)  # Imprime 3

"""
Las tuplas son útiles cuando quieres almacenar un conjunto de valores que no deben cambiar, como las coordenadas de un 
punto en un plano o los meses del año. 
"""

"""
En Python, un conjunto (set) es una estructura de datos desordenada y mutable que no permite elementos duplicados. 
Se utiliza para almacenar una colección de elementos únicos.
"""

"""
También puedes crear un conjunto a partir de una lista utilizando el constructor set(). Por ejemplo:
"""
mi_lista = [1, 2, 2, 3, 4, 4, 5]
mi_set = set(mi_lista)
