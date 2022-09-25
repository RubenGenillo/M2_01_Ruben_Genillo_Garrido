#Creo cuatro variables con valor de entero, flotante, string y booleano
entero = 2
flotante = 2.3
string = "hola"
booleano = True
print( "entero:", entero, type (entero)) #entero: 2 <class 'int'>
print( "flotante:" , flotante , type (flotante)) #flotante: 2.3 <class 'float'>
print( "string:" , string ,type (string)) #string: hola <class 'str'>  
print( "booleano:", booleano, type (booleano)) #booleano: True <class 'bool'>

#Creo dos variables que se llamen nombre y apellido (con mi nombre y mi apellido respectivamente)
nombre = "Rubén"
apellido = "Genillo"

print("nombre + apellido:", nombre + apellido) #nombre + apellido: RubénGenillo
print('nombre + apellido + ".":', nombre + apellido + ".") #nombre + apellido + ".": RubénGenillo.
print("nombre * 3:", nombre * 3) #nombre * 3: RubénRubénRubén

#Creo una variable que se llame nombreCompleto con mi nombre y mi apellido separados con un espacio
nombreCompleto = nombre + " " + apellido
print(nombreCompleto) #Rubén Genillo

#Ahora extraigo solo mi nombre de la variable
print(nombreCompleto[:5]) #Rubén