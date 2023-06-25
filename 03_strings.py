#   Strings

print("Tabulacion\there")
print("Salto de linea\nhere")

#   Una barra invertida le indica a python que ignore el \t, \n, etc
print("\\tEjemplo\\n")

#   Format
#   %s -> strings
#   %i -> integer
#   %d -> double
#   %f -> float

name = "Juan"
last_Name = "Aguilera"
age: int = 21

#   Not recommended, but it works
print("Hello!\nMy name is {} {}.Im {} years old".format(name, last_Name, age))

#   Always better if you use formatting
print("Hello!\nMy name is %s %s.Im %i years old." % (name, last_Name, age))

#   Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language #   Le asigna a cada variable (a,b,c,d,e,f( un espacio de la palabra Python)
print(a)
print(e)
print(f)

#   Division
language_slice = language[1:3]  #   Prints the characters indexed on 1 and 2 positions
print(language_slice)

language_slice = language[1:]   #   Prints from position 1 to the end
print(language_slice)

#   Reverse
reversed_lenguage = language[-3::-1]  #   Negative starts is -1
print(reversed_lenguage)