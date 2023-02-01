
name_1 = input("Nombre_1 : ")
id_1 = input("Id_1: ")
grade_1 = float(input("Grado_1: "))

name_2 = input("Nombre_2: ")
id_2= input("Id_2: ")
grade_2 = float(input("Grado_2: "))

msg1 = name_1 + '(ID ' + id_1 + ') tiene grado: ' + str(grade_1)
print(msg1)
msg2 = name_2 + '(ID ' + id_2 + ') tiene grado: ' + str(grade_2)
print(msg2)

media = (grade_1 + grade_2) / 2.0
print(f"La puntuación media en matemáticas es de {media} puntos")       