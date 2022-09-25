#Creo cuatro variables con valor de entero, flotante, string y booleano
entero = 2
flotante = 2.3
string = "hola"
booleano = True
print(type (entero)) #<class 'int'>
print(type (flotante)) #<class 'float'>
print(type (string)) #<class 'str'>  
print(type (booleano)) #<class 'bool'> 

#Creo dos variables que se llamen nombre y apellido (con mi nombre y mi apellido respectivamente)
nombre = "Rubén"
apellido = "Genillo"

print(nombre + apellido) #RubénGenillo
print(nombre + apellido + ".") #RubénGenillo.
print(nombre * 3) #RubénRubénRubén

#Creo una variable que se llame nombreCompleto con mi nombre y mi apellido separados con un espacio
nombreCompleto = nombre + " " + apellido
print(nombreCompleto) #Rubén Genillo

#Ahora extraigo solo mi nombre de la variable
print(nombreCompleto[:5]) #Rubén