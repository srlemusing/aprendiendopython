"""
Hola mi nombre es Jhonatan Lemus y aqui estoy empezando mi ejercicio
de aprendizaje de python como lenguaje de programacion
echa:28/oct/2022
hra: 09:15AM
"""
print("------------------------------------------------")
#mostrar mensajes en pantalla
print("hola mundo")
print("------------------------------------------------")
#Limpiar consola, se ejecuta el comando cls

#Declarar variable, Guardar valor y mostrar mensaje en pantalla pero concatenado numeros enteros y textos
nombre = "Michelle"
fecha = 2018
print("Hola " + nombre + " gracias por ser mi esposa desde: " + str(fecha))

#Otra forma de concatenar textos y numeros, es la funcion f''
print(f'Hola {nombre} tu numero es: {fecha}')
print("------------------------------------------------")
#Saber el tipo de dato de una variable
print(type(nombre))
print(type(fecha))

print("------------------------------------------------")
#Operadores Aritmeticos

#pedir al usuario ingresar valores
Numero1 = int(input("Ingresa tu primer numero favorito por favor, y presiona enter: "))
Numero2 = int(input("Ingresa tu segundo numero favorito por favor, y presiona enter: "))
print("tus numeros suman: " + str(Numero1 + Numero2)) #suma
print("La diferencia de tus numeros es: " + str(Numero1 - Numero2)) #resta
print("La multiplicacion de tus numeros es: " + str(Numero1 * Numero2)) #multiplicacion
print("La division de tus numeros es: " + str(Numero1 / Numero2)) #division
print("El modulo de tus numeros es: " + str(Numero1 % Numero2)) #modulo

print("------------------------------------------------")
#Operadores lógicos

# AND = todas las opciones son false excepto cuando los dos valores son true
ol1 = True
ol2 = True
print(ol1 and ol2)
# OR = todas las opciones son verdaderas excepto cuando los dos valores son false
ol3 = False
ol4 = False
print(ol3 or ol4)
# NOT = Devulve lo inverso a lo que existe
ol5 = True
ol6 = False
print(not ol6)

print("------------------------------------------------")
#Operadores relacionales
or1 = 4
or2 = 3

# == corresponde a que dos numeros son iguales
print(or1 == or2)
# != corresponde a que numeros son distintosor1 = 4
print(or1 != or2)
# > corresponde a que un numero es mayor que otro
print(or1 > or2)
# >= corresponde a que un numero es mayor o igual que otro
print(or1 >= or2)
# < corresponde a que un numero es menor que otro
print(or1 < or2)
# <= corresponde a que un numero es menor o igual que otro
print(or1 <= or2)
print("------------------------------------------------")

#Operadores de asignación: reasignan nuevo valor a la variable
opa = 9
opa = opa + 1 #primera forma de hacerlo
opa += 1 #segunda forma de hacerlo
print(opa)

opa2 = 5
opa2 = opa2 - 2 #primera forma de hacerlo
opa -= 2 #segunda forma de hacerlo
print(opa2)

opa3 = 1
opa3 = opa3 * 6 #primera forma de hacerlo
opa3 *= 6 #segunda forma de hacerlo
print(opa3)

opa4 = 8
opa4 = opa4 / 12 #primera forma de hacerlo
opa4 /= 12 #segunda forma de hacerlo
print(opa4)

opa5 = 4
opa5 = opa5 % 3 #primera forma de hacerlo
opa5 %= 3 #segunda forma de hacerlo
print(opa5)

print("------------------------------------------------")

#Actividad 1
print("Esta es la respuesta de la actividad 1")
Nro1 = int(input("Ingresa el primer numero, por favor y presiona enter: "))
Nro2 = int(input("Ingresa otro numero, por favor y presiona enter: "))
print("tus numeros suman: " + str(Nro1 + Nro2))
print("La multiplicacion de tus numeros es: " + str(Nro1 * Nro2))
print("¿Ambos numeros son iguales?:" + str (Nro1 == Nro2))
print("¿El primer numero es menor que el segundo?" + str(Nro1 < Nro2))
print("¿El segundo numero es mayor o igual que el primero?" + str(Numero2 >= Numero1))

print("------------------------------------------------")
#Condicional if y condicional else
#Programa que pida y reciba el numero de años de mi computador y mostrar en consola
# si es viejo o nuevo segun su año.
#Indicaciones: si el año es menor o igual a 2 años, es nuevo; si es mayor a 2 años, es viejo.

year = int(input("¿Cuántos años tiene tu computador?: "))

if year >= 0 and year <= 2:
    print("Tu computador es nuevo")
else:
    print("Tu computador es viejo")

#preguntar edad y decir si es mayor de edad o menor de edad
edad = int(input("¿Cuántos años tienes?: "))

if edad >= 18:
    print("Tienes cédula, eres mayor de edad")
else:
    print("Eres menor todavia")

print("¡Hasta pronto!")

print("------------------------------------------------")
#Aplicando condicional elif
#Escuela de conduccion otorga licencia, dependiendo de la edad.
# Indicaciones: Si es menor a 16 entonces no puede obtener licencia
# Si es menor a 18 entonces puede obtener un permiso
# Si es menor a 70 entonces obtiene licencia estandar
# Si es mayor de 70 entonces obtiene una licencia premiun

ed = int(input("Digita tu edad: "))

if ed >= 0 and ed < 16:
    print("Eres menor, aun no puedes obtener licencia para conducir")
elif ed < 18:
    print("Genial, por ahora se te puede otorgar un permiso para conducir")
elif ed < 70:
    print("Super, se te otorgará una licencia estandar.")
else:
    print("Puedes obtener una licencia premium")

print("------------------------------------------------")
#Esta es la segunda actividad del curso
# Programa que pida e ingrese en consola el nombre del cliente y el valor de su compra
# Dependiendo del valor, se otorga descuento de compra o no.

#Se Solicita y se piden los datos del cliente y el valor de su compra total
NombreCliente = input("Hola, cómo te llamas?: ")
ValorCompra = float(input("¿Cuánto se gastó hoy en compras?: "))

#Se formula el descuento del 10%
Des = ValorCompra * 0.10
pf1 = ValorCompra - Des
#Se formula el descuento del 15%
Des2 = ValorCompra * 0.15
pf2 = ValorCompra - Des2
#Se formula el descuento del 20%
Des3 = ValorCompra * 0.20
pf3 = ValorCompra - Des3

if ValorCompra < 80:
    print(f"Lo sentimos {NombreCliente}, su gasto no amerita descuento de la tienda. Debes pagar:" + str(ValorCompra))
elif 80 and ValorCompra < 150:
   print(f"Genial {NombreCliente}, tienes un descuento del 10% y tu valor a pagar es:" + str(pf1))
elif 150 and ValorCompra <= 300:
    print(f"Genial, {NombreCliente}, tienes un descuento del 15% y tu valor a pagar es: " + str(pf2))
elif 300 and ValorCompra < 500:
    print(f"Genial, {NombreCliente}, tienes un descuento del 20% y tu valor a pagar es: " + str(pf3))
else:
    print(f"Gracias {NombreCliente} por tu compra")

print("------------------------------------------------")

#CICLO for
#Ejemplo: Pedir al usuario que ingrese una palabra y que se muestre 10 veces

palabra = input("Por favor, ingresa una palabra: ")
print(f'Tu palabra es: {palabra} ')

for i in range(10):
    print(palabra)

print("------------------------------------------------")

#Ejercicio que me de la raíz cuadrada de los elementos de una lista
cont = 1
for i in [3,4,5,6]:
    print("")
    print(f'Operación número: {cont}')
    print(f'Ahora i vale {i} y su cuadrado es {i ** 2}')
    cont += 1
print("------------------------------------------------")

# Tablas de Multiplicar
nombre = str(input("Hola, cómo te llamas?: "))
numero = int(input("¿Qúe tabla quieres ver?: "))
print("--------------------------------------------------------------")
print(f'Bienvenido {nombre}, esta es la tabla de multiplicar del: {numero}')
print("---------------------------------------------------------------")

for i in range(1,13):
    print(f'{numero} x {i} = {i * numero}')

print("------------------------------------------------")
#Ciclo While: Se usa cuando no conocemos el numero de veces que se debe usar una instruccion
# Ejemplo: calculando indice de masa corporarl - IMC , usaremos condiciones simples y aninadas.

conta = 0

while conta != 2:
    conta = int(input("¿Deseas continuar calculando el IMC?: 1. Si y 2. No \n"))
    if conta == 1:
        esta = float(input("Digita tu estatura actual: "))
        pes = float(input("Cuánto pesas actualmente?: "))
        r = round(pes / (esta ** 2), 2)
        if r < 18.5:
            print(f'Tu IMC es: {r}: Estas bajo de peso')
        elif 18.5 < r < 24.99:
            print(f'Tu IMC es: {r}: Tienes un peso normal')
        elif 25 < r < 30:
            print(f'Tu IMC es: {r}: Tienes sobrepeso')
        elif r > 30:
            print(f'Tu IMC es: {r}: Estas obeso')
    elif conta == 2:
        print("Hasta pronto!")
print("-----------------------------------------------------")
print("Gracias por usar esta aplicación")
print("-----------------------------------------------------")

#Actividad 3, aplicando ciclos While y condiciones if simples y aninadas.
#Tenemos 5, se pide el nombre del estudiante y la nota de cada materia y se calculará el promedio

materias = 5
contador = 1
sumatoria = 0

NombreEs = input("Buenos dias, ¿Cuál es tu nombre?: ")
print("De acuerdo, vamos a solicitarte tus asignaturas y tus calificaciones, medirémos tu promedio del semestre")
print("----------------------------------------------------------------------")
while contador <= materias:
    nomMateria = input("Ingresa el nombre de la (" + str(contador) + ") asignatura: ")
    nTA = float(input("cual fué tu nota final en la asignatura: " + str(nomMateria) + ": " ))
    sumatoria = sumatoria + nTA
    contador = contador + 1
    pro = sumatoria/materias
    # ¿Cuál es tu nombre y qué promedio obtuviste?
print("----------------------------------------------------------------------")
print(f'{NombreEs}, dado lo anterior tu promedio en este semestre es de: {pro} ')
print("----------------------------------------------------------------------")

#Funciones
#Los valores que se recibe la funcion se denominan parámetros
#Los resultados que arroja una funcion, se denominan Argumentos.

#Definir y llamar una funcion, ejemplo sencillo:
def saludo():
    print("Este es un saludo")
saludo()

#Funcion sencillo con una instruccion
def suma():
    print(f'La suma es: {2+9}')
suma()

#Funcion con parámetros
def esPar(numero):
    if numero % 2 == 0:
        print(f'El numero: {numero} es par')
    else:
        print(f'El numero: {numero} es impar')
esPar(3)

#Funcion con parámetros, debes darle valor a y valaor a b, sino, te arroja error la funcion
def resta(a = None, b = None):
    if a == None or b == None:
        print("Error, debes ingresar dos numeros a la funcion")
        return
    return a - b
r = resta(1, 5)
print(f'La resta es: {r}')

#Funcion que me permita ingresar obligatoriamente el numero
# de la tabla de multiplicar que deseo ver:
def tablaM(nm = None): #Parametro
    if nm == None:
        print("Lo siento, debes ingresar un numero")
    else:
        print(f'Esta es la tabla de Multiplicar del {nm}')
        for i in range(1, 13):
            print(f'{nm} x {i} = {nm * i}')
tablaM(5) #Argumento

#Funciones posicionales, tenemos: args y kwargs

# Ejemplo con los args = nos permite definir la función sin conocer de que informacion se trata.
#programa que me muestra la suma de los elementos que yo quiera. Recibe clos agrumentos como una tupla
def operac(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
resul = operac(3,6,7,1,2,4,5)
print(resul)

#programa que me da el nombr y los idiomas preferidos que yo desee.
def idiomas(nombre, *idio):
    print(f'Hola {nombre}')
    print(f'tus lenguajes favoritos son: {idio}')
idiomas("Diego", "Español", "Ingles", "Frances", "Italiano")

#kwargs = Al contrario, no permite saber el contenido de información que se trata,
# esto porque usamos los pares clave y valor. Recibe clos agrumentos como un diccionario.

#Ejemplo que ingresa un nombre y lenguaje favoritos sin importar la cantidad, pero definimos sus valores por cariables
def lenguajes(nombre, **kwargs):
    print(f'Hola, {nombre}')
    print("Buscando informacion acerca de tus lenguajes favoritos...")
    print("Cargando informacion... \n")

    print("Informacion: ")
    contad = 0
    for i in kwargs:
        contad += 1
        print(f'Tú {contad} lenguaje favorito es: {kwargs[i]} ')

lenguajes("Gahel", lenguaje1 = "Italian", lenguaje2 = "Portugues")


#Actividad 4: Conversos de Monedas
print("------------------------------------------------------")
print("Bienvenido, este es tu conversor de Monedas           | \n")
print("------------------------------------------------------")

def cm(mdactual, vlrmd, mdAco):

    if mdactual == 1:
        def dolarT():
            if mdAco == "1":
                print(f'USD {vlrmd} Dólares equivalen a $ {vlrmd * 3750} pesos Colombianos')
            elif mdAco == "2":
                print(f'USD {vlrmd} Dólares equivalen a ¥ {vlrmd * 6.37} Yuanes')
            elif mdAco == "3":
                print(f'USD {vlrmd} Dólares equivalen a € {vlrmd * 0.76} LibrasEsterlinas')
            else:
                print("No se reconoce la Moneda a convertir")
        dolarT()

    elif mdactual == 2:
        def euroT():
            if mdAco == "1":
                print(f'€ {vlrmd} Euros equivalen a $ {vlrmd * 4000} pesos Colombianos')
            elif mdAco == "2":
                print(f'€ {vlrmd} Euros equivalen a  ¥ {vlrmd * 6.93} Yuanes')
            elif mdAco == "3":
                print(f'€ {vlrmd} Euros equivalen a  $ {vlrmd * 0.83} LibrasEsterlinas')
            else:
                print("No se reconoce la Moneda a convertir")
        euroT()
    else:
        """
        50 dólares en pesos Colombianos es igual a: 50*3750
        30 euros en Yuanes es igual a: 30*6.93
        15 euros en Libras Esterlinas es igual a: 15*0.83
        """
        print("No se reconoce la Moneda que deseas Convertir")

mdactual = int(input("Ingrese su moneda local y presione Enter: \n 1. Dolar \n 2. Euro \n \n--> "))
print("")
vlrmd = float(input("Digita el valor a convertir y presione enter: \n --> "))
print("")
mdAco = input(
    "Hacia qué moneda quieres hacer la conversión? \n1. Pesos Colombianos"
    "\n2. Yuanes \n3. LibrasEsterlinas \n \n--> ")
print("")
cm(mdactual, vlrmd, mdAco)

print("------------------------------------------------------")
print("Hasta la próxima, amigo!                              | \n")
print("------------------------------------------------------")