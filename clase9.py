# funciones

# print('Hola')
# len('Hola')
# print(len('Hola'))
# print(len('Hola'))
# print(len('Hola'))
# print(len('Hola'))
# print(len('Hola'))

# cant_letras = 0
# for letra in 'Hola':
#     cant_letras += 1
    
# print(cant_letras)

# cant_letras = 0
# for letra in 'Hola':
#     cant_letras += 1
    
# print(cant_letras)
# cant_letras = 0
# for letra in 'Hola':
#     cant_letras += 1
    
# print(cant_letras)

# 2 + 2
# 2 + 2
# 2 + 2
# 2 + 2
# 2 + 2
# 2 + 2
# 2 + 2
# 2 + 2
# 2 + 2
# 2 + 2
# 2 + 2
# 2 + 2



# cant_letras = 0
# for letra in 'Hola':
#     cant_letras += 1
    
# print(cant_letras)
# cant_letras = 0
# for letra in 'Hola':
#     cant_letras += 1
    
# print(cant_letras)
# cant_letras = 0
# for letra in 'Hola':
#     cant_letras += 1
    
# print(cant_letras)


# ====================================================================
# ====================================================================

# def NOMBRE(PARAMETROS??): # correcto nombramiento de las funciones
#     SENTENCIAS
#     return EXPRESION??
    
# ====================================================================
# ====================================================================

# def mostrar_palabra():
#     print('Perro')
#     # return
    
# mostrar_palabra() 
# valor_retornado = mostrar_palabra()
# print(valor_retornado)


# def retornar_palabra():
#     return 'Perro'

# retornar_palabra()
# print(retornar_palabra())
# valor_retornado = retornar_palabra()
# print(valor_retornado)
# print(type(retornar_palabra()))
# print(valor_retornado * 5)
# print(retornar_palabra() * 5)
# nuevo_texto = f'{retornar_palabra()} es un animal'
# print(nuevo_texto)


# def devolver_una_lista():
#     return list(range(6))

# valores = devolver_una_lista()
# print(valores)
# print(valores[1:4])
# print(devolver_una_lista())
# print(devolver_una_lista()[1:4])

# ====================================================================
# ====================================================================

# scope ( alcance )

# valor1 = 4

# def sumar_numeros():
#     # print(valor1)
#     # global valor1
#     # valor1 = 15
#     # print(valor1)
#     valor2 = 56
#     valor3 = 15
#     return valor1 + valor2 + valor3

# valor1 = 4

# suma_de_valores = sumar_numeros()

# print(valor1)
# # print(valor2)

# # valor1 = 4

# print(suma_de_valores)

# ====================================================================
# ====================================================================

# def suma(valor1, valor2):
#     return valor1 + valor2

# print(suma(15, 16))
# valor1 = 15
# valor2 = 15
# print(suma(valor1, valor2))

# ====================================================================
# ====================================================================

# lista = [1,2,3,4,5,7,1,1,5,21,5,2,2,3,4,25,2]
# tupla = (1,2,3,4,5,7,1,1,5,21,5,2,2,3,4,25,2)

# print(sum(lista))

# def mi_sum(coleccion_de_valores):
#     suma = 0
#     for valor in coleccion_de_valores:
#         # print('Sumando el valor', valor)
#         suma += valor
#     return suma
#     # print(suma)

# print(mi_sum(lista))
# print(mi_sum(tupla))
# mi_sum(lista)

# ====================================================================
# ====================================================================

# print(len('Hola'))
# print(len('ricardo lo mas'))

# # cant_letras = 0
# # for letra in 'Hola':
# #     cant_letras += 1
    
# # print(cant_letras)

# def contame_las_letras(palabras_a_contar): # snake_case
#     cant_letras = 0
#     for letra in palabras_a_contar:
#         cant_letras += 1
#     return cant_letras

# print(contame_las_letras('Hola'))
# print(contame_las_letras('ricardo lo mas'))

# ====================================================================
# ====================================================================

# def desordeno_tus_argumentos(param1, param2, param3, param4, param5):
#     # tupla = (param3, param5, param4, param1, param2)
#     # return tupla
#     return param3, param5, param4, param1, param2

# valor1 = 1
# print(desordeno_tus_argumentos(valor1,2,3,4,5))
# primero, segundo, tercero, cuarto, quinto = desordeno_tus_argumentos(valor1,2,3,4,5)

# # primero, segundo, tercero, cuarto, quinto = (1,2,3,4,5)
# print(primero)
# # print(segundo)
# # print(tercero)
# # print(cuarto)
# # print(quinto)

# ====================================================================
# ====================================================================

# Momentos de una funcion
# definimos la funcion
# llamo a la funcion ejecuta su codigo
# revisa si tiene un return
# si no tiene un return devuelve None por defecto
# si tiene un return devuelve lo que tiene a continuacion el return

# ====================================================================
# ====================================================================

# Ej - Par o Impar
# Realizar una función llamada par_o_impar:

# Recibirá un número por parámetro
# Imprimirá Par si el número es par
# Imprimirá Impar si el número es impar
# Si se ingresa algo que no sea número debe indicar que se ingrese un número. (Para los más audaces) 

# v1
# def par_o_impar(numero):
#     if numero%2==0:
#         return 'Par' 
#     else:
#         return 'Impar'
        
# print(par_o_impar(int(input('Ingresame un numero y te digo que es: '))))


# # v2
# def par_o_impar(numero):
#     for digito in numero:
#         if digito not in '0123456789':
#             return 'Debe ingresar un numero.'
    
#     numero_casteado = int(numero)
    
#     if numero_casteado%2==0:
#         return 'Par' 
#     else:
#         return 'Impar'

# print(par_o_impar(input('Ingresame un numero y te digo que es: ')))

# ====================================================================
# ====================================================================

# Desafio - Año Bisiesto

# ====================================================================
# ====================================================================
# 
# Realizar una función llamada anio_bisiesto:

# Recibirá un año por parámetro
# Imprimirá “El año es bisiesto” si el año es bisiesto
# Imprimirá “El año no es bisiesto” si el año no es bisiesto
# Si se ingresa algo que no sea número, debe indicar que se ingrese un número.

# Información a tener en cuenta:

# Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, 
# aunque los múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 
# 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.

# v1
# def anio_bisiesto(anio):
#     if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
#         return 'El año es bisiesto'
#     return 'El año no es bisiesto'

# print(anio_bisiesto(2023))


# v2
# def anio_bisiesto(anio):
#     for caracter in anio:
#         if caracter not in '0123456789':
#             return 'Debe ingresar un numero.'
    
#     anio_int = int(anio)
    
#     if anio_int % 4 == 0 and (anio_int % 100 != 0 or anio_int % 400 == 0):
#         return 'El año es bisiesto'
#     return 'El año no es bisiesto'


# anio = input('Ingrese un anio:')
# print(anio_bisiesto(anio))


# v3
# def anio_bisiesto(anio):
#     for caracter in anio:
#         if caracter not in '0123456789':
#             return 'Debe ingresar un numero.'
    
#     anio_int = int(anio)
    
#     if anio_int % 4 == 0 and (anio_int % 100 != 0 or anio_int % 400 == 0):
#         return 'El año es bisiesto'
#     return 'El año no es bisiesto'

# while True:
#     anio = input('Ingrese un anio:')
#     print(anio_bisiesto(anio))












