
#instruccion lower para quitar las mayusculas de lo codigo
cadena1 = 'CADENA ESCRITA EN MAYUSCULAS'
cadena2 = cadena1.lower()
print(cadena2)

#la siguiente linea muestra una lista de atributos y metodos disponibles para el objeto
print(dir(cadena1))

#La instruccion capitalize pone la primera letra
print(cadena2.capitalize())

cadena_larga= ''' Esto es un ejemplo 
de una cadena larga con tres comillas
para ejemplificar como se divide una cadena 
con la instruccion split'''
print(cadena_larga.split(" "))