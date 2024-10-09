
from Funciones import nuevo_tema, nuevo_subtema

print(__file__)

exit()
print('hola mundo mi nombre es "Sigfrido"') 
print('saludos')

def error():
    vfkjbfjkhfedñlgherfklfeghklfdshklfghvkishklj

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)
numero  = 500   
print ("factorial de ", numero, " es ", factorial(numero))


nuevo_tema("variables")
edad = 20
print("edad: ", edad)

altura = 1.65
print("altura: ", altura)

nombre = "Eduardo"
print("nombre: ", nombre)

es_trabajador = True
print("es_trabajador: ", es_trabajador)




nuevo_tema("listas")

frutas = ['manzanas', 'peras', 'piñas', 'naranjas', 'guayabas', 'papayas']
print('frutas: ', frutas)

varias_cosas = ['Escuela', 23, True, frutas]
print('varias_cosas', varias_cosas)

"""
    Seleccionando un elemento
    Comentario de multiples lineas
"""
print('frutas[2]: ', frutas[2])

print('frutas[-1]: ', frutas[-1])
print('frutas[-2]: ', frutas[-2])

print('frutas[1:5]: ', frutas[1:5])
print('frutas[1:5:2]: ', frutas[1:5:2])

# agregando un elemento al final
frutas.append('fresas')
print("frutas: ", frutas)
# quitando un elemento
frutas.remove('naranjas')
print("frutas: ", frutas)
#insertando un elemento en la posición descrita
frutas.insert(4, 'kiwi')
print("frutas: ", frutas)

#creando una lista vacia
calificaciones = []
libros = list()
print('calificaciones: ', calificaciones)
print('libros: ', libros)

frutas.reverse()
print("frutas: ", frutas)
frutas.sort()
print("frutas: ", frutas)

nuevo_tema("diccionarios")

persona ={"nombre": "Pedro", 
          "apellido": "Pérez",
          "edad": 48, }

# print('persona: ', persona)
# persona.update({"nombre": "Juan"})
# persona['nombre'] ='julio'
# print("Imprmiendo nuevamente persona: ", {++a, "nombre" : "javier"})
# exit()
# print("persona.keys(): ", persona.keys())
# print("persona.values(): ", persona.values())

# print('persona.get("nombre"):', persona.get("nombre"))
# print('persona.get("estatura"):', persona.get("estatura"))

# print("persona.items(): ", persona.items())

nuevo_tema("Ciclos")
nuevo_subtema("for")
for i in range(10):
    print(i)

print("#########")
for i in range(3,10):
    print(i)

print("#########")
for i in range(3,10, 2):
    print(i)

print ("len(frutas):", len(frutas))

for f in frutas:
    print(f)
print("######### con len")
for indice in range(len(frutas)):
    print("Indice ", indice , frutas[indice])

print("######### con enumerate")
for indice, fruta in enumerate(frutas):
    print(indice, fruta)

print("######### for en un diccionario")
for key, value in persona.items():
    print(key, value)

print(__file__)