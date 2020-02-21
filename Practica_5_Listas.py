##Ejercicio 1 F
## Hacer un programa que guarde la siguiente lista en una variable: [elefante, jirafa,
## mono], luego pida el nombre de otro animal, lo agregue a la lista e imprima en pantalla el
## cuarto animal de la lista.


##animales=["elefante","jirafa","mono"]
##a=input("Ingrese un animal:")
##animales.append(a)
##print(animales[3])

##Ejercicio 2 F
##Definir una función llamada mostrarEnUnaLinea que tome una lista de enteros y muestre
##todos sus elementos en una linea separados por espacios.

##def mostrarEnUnaLinea(listaEnteros):
##    for i in listaEnteros:
##        print(i,end=" ")
##
##lista=[1,2,3,4,5,6]
##mostrarEnUnaLinea(lista)


##Ejercicio 3 F
## Definir una función llamada divisores que tome un entero y devuelva la lista de divisores de
## ese entero

##def divisores (n):
##    listaDiv=[]
##    for i in range(1,n):
##        if n%i==0:
##            listaDiv.append(i)
##    return listaDiv
##n=int(input("Ingrese un numero:"))
##print(divisores(n))


##Ejercicio 4 F
##Definir una función llamada laMasCorta que tome dos listas y devuelva la que tenga menos
##elementos. Si tienen igual cantidad, deberá devolver la primera.

##def laMasCorta(lista1,lista2):
##    if len(lista1) <= len(lista2):
##        return lista1
##    return lista2
##
##l1=[12,3,4,5,6,3,3,3,3,3,3]
##l2=[1,2,3,4,5,6,7,8]
##print(laMasCorta(l1,l2))


##Ejercicio 5 F
##Definir una función llamada sonFactores que tome un entero n y una lista de enteros, y
##devuelva True si los números de la lista son factores de n (es decir, si n es divisible por todos
##ellos).


##def sonFactores(n,lista):
##    for i in range(len(lista)):
##        if not n%lista[i]==0:
##            return False
##    return True
##
##n=30
##lista=[3,15,7]
##print(sonFactores(n,lista))




## Ejercicio 6 F
## Definir una funcion que tome una lista y devuelva True si tiene al menos un elemento repetido,
## y False en caso contrario.


##def tieneRepetido(lista):
##    for i in range(len(lista)):
##        for j in range(i+1,len(lista)):
##            if lista[i]==lista[j]:
##                return True
##    return False
##
##lista=[1,2,3,4,5,5]
##if tieneRepetido(lista):
##    print("True")
##else:
##    print("False")

## Ejercicio 7 F
## Definir una función llamada dondeAparece que tome una lista de enteros y un entero llamado
## blanco como parámetros, y devuelva el primer índice donde blanco aparece en el arreglo, si lo
## hace, y -1 en caso contrario


##def dondeAparece(lista,blanco):
##    for i in range(len(lista)):
##        if lista[i] == blanco:
##            return i
##    return -1
##
##lista=[1,2,3,4]
##blanco= 3
##print(dondeAparece(lista,blanco))


##Ejercicio 8 F
##Hacer una función que tome una lista de números decimales y devuelva el promedio de los
##elementos


##def promedio(lista):
##    suma=0
##    for i in range(len(lista)):
##        suma=suma+lista[i]
##    return suma
##
##lista=[10,1,10]
##print(promedio(lista)/len(lista))



## Ejercicio 9 F
## Escribir una función llamada maximo que tome una lista de números y devuelva el valor del
## máximo elemento.

##def mayor(lista):
##    max=lista[0]
##    for num in lista:
##        if num > max:
##            max=num
##    return max
##
###Programa Principal
##lista = [5,-12,9,10,2,0]
##maximo = mayor(lista)
##print("El mayor de la lista ",lista," es:",maximo)



##Ejercicio 10 F
##Escribir una función llamada maximoIndice que tome una lista de números y devuelva el
##índice del máximo elemento

##def indiceDelMax(lista):
##    pos=0
##    for i in range(len(lista)):
##        if lista[i] > lista [pos]:
##            pos=i
##    return pos
##
##lista=[6,7,8,9,0]
##print(indiceDelMax(lista))



## Ejercicio 11 F
## Escribir una función llamada maximoEntre que tome una lista de números y dos enteros a y b
## menores que la longitud de la lista y devuelva el índice del máximo elemento considerando solo
## los que están entre el índice a y el índice b.


## Ejercicio 12 F
## Escribir una función llamada intercambiar que tome una lista de números s y dos enteros
## positivos a y b menores que la longitud de la lista y cambie el elemento ubicado en s[a] por el
## elemento ubicado en s[b]. Ojo, esta función no debe devolver una lista, sino modicar la que
## toma como parámetro.


##def intercambiar(lista,a,b):
##    aux=lista[a]
##    lista[a]=lista[b]
##    lista[b]=aux
##
##lista=[1,2,3,4,5,6]
##a=1
##b=5
##intercambiar(lista,a,b)
##print(lista)



##Ejercicio 13 F
##Escribir una función llamada frecuencia que tome una lista de enteros s y otro entero n como
##parametros y devuelva la cantidad de veces que aparece n en s.

##def frecuencia(lista,n):
##    cont=0
##    for i in range(len(lista)):
##        if lista[i]==n:
##            cont=cont+1
##    return cont
##
##lista=[1,1,1,1,1,1,2,2,2,2]
##n=1
##print(n,"Aparece en la lista",lista,frecuencia(lista,n),"veces")




## Ejercicio 14 F
## Definir una función llamada interseccion que tome dos listas sin repetidos y devuelva una
## nueva lista que contenga sólamente aquellos elementos que estén ambas listas

##def esta(entero,lista):
##    for i in lista:
##        if i==entero:
##            return True
##    return False
##
##
##def interseccion(lista1,lista2):
##    nuevaLista=[]
##    for elemento in lista1:
##        if esta(elemento,lista2):
##            nuevaLista.append(elemento)
##    return nuevaLista
##
##lista1=[1,2,5,7,4,9]
##lista2=[1,5,9,0]
##print(interseccion(lista1,lista2))


## Ejercicio 15 F
## Definir una función llamada union que tome dos listas sin repetidos y devuelva una nueva lista
## que contenga los elementos de ambas listas. Ojo, la lista de retorno debe no tener repetidos.


##def esta (entero,lista):
##    for elemento in lista:
##        if elemento == entero:
##            return True
##    return False
##
##def sinRepetidos(lista):
##    nuevaLista=[]
##    for elemento in lista:
##        if not esta (elemento,nuevaLista):
##            nuevaLista.append(elemento)
##    return nuevaLista
##
##def union(lista1,lista2):
##    return sinRepetidos(lista1+lista2)
##
##lista1=[1,2,3,4,5,6]
##lista2=[1,2,3,4,5,6,7,8,6,8,7]
##print(union(lista1,lista2))


## Ejercicio 16 F
## Definir una función llamada diferencia que tome dos listas sin repetidos y devuelva una
## nueva lista que contenga los elementos la primera que no estén en la segunda.


##def esta (entero,lista):
##    for elemento in lista:
##        if elemento == entero:
##            return True
##    return False
##
##def diferencia(lista1,lista2):
##    nuevaLista=[]
##    for elemento in lista1:
##        if not esta(elemento,lista2):
##            nuevaLista.append(elemento)
##    return nuevaLista
##
##lista1 = [1,2,3,4,5,6,7,8,9]
##lista2 = [1,3,12,13,15,6,18]
##print(diferencia(lista1,lista2))


## Ejercicio 17 F
## Definir una función llamada mcd que tome dos enteros positivos y devuelva el máximo común
## divisor usando funciones de los ejercicios anteriores.


##def esta (entero,lista):
##    for elemento in lista:
##        if elemento==entero:
##            return True
##    return False
##
##def interseccion(lista1,lista2):
##    lista_Nueva=[]
##    for i in lista1:
##        if esta(i,lista2):
##            lista_Nueva.append(i)
##    return lista_Nueva
##
##def divisores(n):
##    divisoresDeN=[]
##    for i in range(1,n+1):
##        if n%i==0:
##            divisoresDeN.append(i)
##    return divisoresDeN
##
##def maximo(lista):
##    max=lista[0]
##    for i in lista:
##        if i > max:
##            max=i
##    return max
##
##def mcd (a,b):
##    divA=divisores(a)
##    divB=divisores(b)
##    divComunes=interseccion(divA,divB)
##    MCD=maximo(divComunes)
##    return MCD
##a=int(input("Ingrese un numero: "))
##b=int(input("Ingrese un numero: "))
##
##print (mcd(a,b))



## Ejercicio 18 F
## Definir una función que tome un entero n y devuelva los primeros n primos.

##def esPrimo(n):
##    for i in range(2,n):
##        if n%i==0:
##            return False
##    return True
##
##n=int(input("Ingrese un numero:"))
##i=1
##primos=[]
##
##cont=1
##while cont<=n:
##    if (esPrimo(i)):
##        primos.append(i)
##        cont=cont+1
##    i=i+1
##print(primos)




##Ejercicio 19 F
## Definir una función que tome un entero n y devuelva la lista de los primos que aparecen al
## factorear n. Ejemplo, para 24, la lista debe ser: [2, 2, 2, 3]

##def esPrimo(n):
##    for i in range(2,n):
##        if n%i==0:
##            return False
##    return True
##
##def factPrimos(n):
##    lista=[]
##    i=2
##    while i<=n:
##        if n%i==0 and esPrimo(i):
##            lista.append(i)
##            n=n/2
##        else:
##            i=i+1
##    return lista
##
##n=24
##print(factPrimos(n))



## Ejercicio 20 F

## a) Definir una función que tome una lista de números s y un número decimal x y
## devuelva la cantidad de elementos de s que sean menores que x
##def contarMenores(lista,x):
##    cantElementos=[]
##    for num in lista:
##        if num < x:
##            cantElementos.append(num)
##    return cantElementos
##
##lista=[1,2,3,4,5,6,7,8,9]
##print(contarMenores(lista,9))



##def cantMenores(lista,decimal):
##    cont=0
##    for deci in lista:
##        if deci < decimal:
##            cont=cont+1
##    return cont
##lista=[1,2,3,4,5,6,7,8,9]
##print(cantMenores(lista,9))


## b) Si se pone como condición que s siempre esté ordenada de mayor a menor, ¾cómo
## podría modicarse el programa para que haga menos iteraciones?


## Ejercicio 21 F
## Denir una función que tome una lista de números s y un número decimal x y cambie todos
## los elementos menores que x por 0.
## Ej:
## Para
## s = [1, 4.1, 6.3, 2, 3.2, 8]
## x = 3
## el la lista debe pasar a ser:
## s = [0, 4.1, 6.3, 0, 3.2, 8]


##def cambiaMenoresPorX(s,x):
##
##    for i in range(len(s)):
##        if s[i] < x:
##            s[i]=0
##    return s
##
##s = [1, 4.1, 6.3, 2, 3.2, 8]
##x = 3
##print(cambiaMenoresPorX(s,x))


## Ejercicio 22 F
##Escribir un programa que pida al usuario una cadena, y luego escriba en pantalla la cantidad
## de veces que aparece cada letra (sin mostrar las que no aparecen). Ej:
## Palabra ingresada: "conocido"
## c : 2
## d : 1
## i : 1
## n : 1
## o : 3


def aparece (letra,cadena):
    for char in cadena:
        if char == letra:
            return True
    return False

def sinRepetidas(cadena):
    nuevaCadena=""
    for char in cadena:
        if not aparece(char,nuevaCadena):
            nuevaCadena=nuevaCadena+char
    return nuevaCadena

def cantApariciones(letra,cadena):
    cont=0
    for char in cadena:
        if char==letra:
            cont=cont+1
    return cont

def conocido(palabra):
    sinRep=sinRepetidas(palabra)
    for char in sinRep:
        veces=cantApariciones(char,palabra)
        print(char,":",veces*"*")

palabra = "conocido"
conocido(palabra)



## Ejercicio 24 F
## Auxilio Mecánico
## En una empresa de auxilio mecánico existen dos coberturas para los clientes, Oro y Plata. Los
## clientes con cobertura Oro tienen más beneficios que los de cobertura Plata y pagan mensualmente
## un abono mayor. Por ejemplo los clientes Oro tienen usos ilimitados y los clientes Plata
## sólo hasta 5. El sistema ya está funcionando y tenemos que implementar una función particular
## que devuelva el costo para un cliente de un servicio particular.


## Se cuenta con las siguientes funciones y sus valores de retorno:

## cobertura(cliente): retorna un string con los valores "Oro" o "Plata", correspondiente al tipo de cobertura del cliente.

## usados(cliente): retorna un entero que representa la cantidad de servicios que ya utilizó el cliente.

## radioDeCobertura(cliente, localidad): devuelve True si el cliente se encuentra dentro del radio de cobertura cubierto por la empresa.

## Al recibir un llamado el operador telefónico solicita el número de cliente, la localidad para la
## que solicita la asistencia y le informa el costo del servicio teniendo en cuenta que el servicio no
## tendrá costo para los clientes Oro que estén dentro del área de cobertura y para los clientes Plata
## que les quedaran servicios para usar y estuvieran dentro dicha área. Pagarán $50, los clientes
## Plata dentro del área de cobertura pero ya sin servicios gratis. Pagarán $30 extra los clientes que
## estén fuera del área de cobertura. Observación, los dos últimos montos pueden ser acumulativos.
## Hacer una función llamada pagara que dado un cliente y una localidad devuelva el costo del
## servicio para el cliente.

def pagara (cliente,localidad):
    costo=0
    if not radioDeCobertura(cliente, localidad):
        costo=30

    if cobertura(cliente)==plata and usados(cliente)>5:
        costo=costo+50

    else:
        if radioDeCobertura(cliente, localidad) == True:
            costo=costo+0
    return costo


nroCliente=int(input("Ingrese un numero:"))
localidad=int(input("Ingrese su localidad:"))




##Ej 24, Practica 5
def pagara(cliente, localidad):
    total = 0
    if not radioDeCobertura(cliente, localidad):
        total = total + 30
    if cobertura(cliente) == "plata" and usados (cliente) >5:
        total = total + 50

    return total







##Ejercicio 25 F
##Hacer una función que automatice el control vehicular en rutas nacionales. Hacer el control
##para la Ruta Nacional 8 durante un día completo, se debe controlar que los automóviles no
##superen 100 km/h y en caso de hacerlo se les enviará una multa a sus hogares, si es reincidente
##la multa se duplica. Para ello cuenta con las siguientes funciones.
##darPatentes(ruta): Dada una ruta nacional devuelve una lista con todas las patentes de los
##autos que pasaron en el día.
##controlVelocidad(patente): Recibe un número de patente y devuelve la velocidad a la que
##cruzó el radar dicho automóvil.
##reincidente(patente): Devuelve True en caso de que la patente ya tenga multas por exceso
##de velocidad.
##costoActual(): No recibe parámetros y devuelve el costo por superar la velocidad permitida.
##enviarMulta(patente, costo): Manda una multa al domicilio del propietario del automóvil
##con el costo






















