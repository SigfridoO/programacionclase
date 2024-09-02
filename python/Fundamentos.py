print('hola mundo mi nombre es "Sigfrido"') 
print('saludos')

# Este es una función para poner el encabezado de los temas
def nuevo_tema(tema):
    print("==============", tema, "==============")

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
print()

