#el promedio de un alumno que ha cursado 5 materias (Español, Matemáticas, Economía, Programación, Ingles).
print("Ingrese calificaion final de asigantura español:")
español=input()
print("Ingrese calificaion final de asigantura matematicas:")
matematicas=input()
print("Ingrese calificaion final de asigantura economia:")
economia=input()
print("Ingrese calificaion final de asigantura ingles:")
ingles=input()
print("Ingrese calificaion final de asigantura programacion:")
programacion=input()

español1= int(español)
matematicas2= int(matematicas)
economia3= int(economia)
ingles4= int(ingles)
programacion5= int(programacion)

suma= español1+matematicas2+ economia3+ ingles4+ programacion5
P= suma / 5
print('El promedio general del alumno con las 5 asiganturas es: ',(P))


