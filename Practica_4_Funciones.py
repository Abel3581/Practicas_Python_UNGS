# PRACTICA 4 FUNCIONES

##Escribir un programa en Python (en la computadora) que tome un
##n´umero decimal x y muestre por pantalla el resultado del siguiente
##c´alculo:
##
##  Raiz de log(|1 − x|)
##
##Recuerden que para usar las funciones matem´aticas de Python, hay
##que incluir arriba de todo:
##im p o r t math


##import math
##
##x=float(input("Ingrese un numero decimal:"))
##res=math.sqrt(math.log10(abs(1-x)))
##print(res)



##def mostrarGuion( ):
##    print("-",end="")
##
## Cuando hagan sus propias funciones, guardenlas en un archivo con
## extensi´on .py. Por ejemplo: misFunciones.py
## Cuando las quieran usar en otro archivo, escriban arriba de todo:
## f rom m i s F u n c i o n e s im p o r t *
## sin la extension (.py).
## Nota: Se pueden guardar muchas definiciones de funciones en un
## mismo archivo.


##def imprimirdosveces(unacadena):
##    print(unacadena)
##    print(unacadena)
##imprimirdosveces("hola")

##def mostrarGuion () :
##    print ( "-" , end="" )
##
##mostrarGuion()

##def mostarDosveces(unacadena):
##    print(unacadena)
##    print(unacadena)
##argumento="!! Funciones ¡¡"
##mostarDosveces(argumento)




##Ejercicio 1 F
##Hacer un programa para cada inciso que pida al usuario un número decimal x y muestre por
##pantalla el resultado de evaluar las siguientes fórmulas:

#a)  Raiz de x
##import math
##x=float(input("Ingrese un numero:"))
##res=math.sqrt(x)
##print(res)

#b) Modulo de x
##import math
##
##x=float(input("Ingrese un numero:"))
##res=abs(x)
##print(res)


#c) Modulo (x-3)

##import math
##x=int(input("Ingrese un numero:"))
##res=abs(x-3)
##print(res)


#d) Raiz de modulo (x-5)

##import math
##x=int(input("Ingrese un numero:"))
##res=math.sqrt(abs(x-5))
##print(res)


##Ejercicio 2 F
##Teniendo estas deniciones de funciones:

##def cuak ( ) :
##    chan ( )
##    print ( " pienso que " , end="" )
##    chan ( )
##
##def chan ( ) :
##    print ( "yo" , end="" )
##    plin ( )
##
##def plin ( ) :
##    print ( "." )
##
###Indicar qué se imprime en pantalla luego de ejecutar este programa:
##print ( "No , yo " , end="" )
##cuak ( )
##print ( "Yo " , end="" )
##chan ( )


##Ejercicio 3 F
##El objetivo de este ejercicio es entender cómo escribir y llamar funciones que toman parámetros.
##a) Escribir la primera línea de una función llamada arnaldito que tome tres parámetros: un entero
## y dos cadenas. (Escribir sólamente la primera linea o encabezado)


##def arnaldito(entero,cad1,cad2):


##b) Escribir una línea de código que llame a arnaldito, pasando como parámetros al
##valor 11, el nombre de tu primera mascota y el nombre de la calle en la cual creciste


##def arnaldito(valor,mascota,calle):
##    print(valor)
##    print(mascota)
##    print(calle)
##arnaldito(11,"KITY","GARIN")


## Ejercicio 4 F
## a) Escribir una función que reciba como parámetro una cadena y la muestre en pantalla
## 3 veces.

##def imprimoTres(cadena):
##    print(cadena)
##    print(cadena)
##    print(cadena)
##cad=input("Ingrese una cadena:")
##imprimoTres(cad)


## b) Guardar esta definición de función en un archivo.
# Guardar como misfunciones.py




### c)Hacer un programa que le pida al usuario una cadena y que la muestre en pantalla
## 3 veces utilizando la función definida anteriormente.


##from misfunciones import*
##imprimoTres(cad)


#5)
#a) Escribir una función que reciba dos números reales como parámetros y retorne su
# promedio

##def promedio(num1,num2):
##    res=(num1+num2)/2
##    return res
##n1=float(input("Ingrese un numero:"))
##n2=float(input("Ingrese un numero:"))
##print(promedio(n1,n2))



##b) Hacer un programa que pida al usuario dos números reales y muestre por pantalla
##el resultado de llamar a la función del primer inciso


##A=float(input("Ingrese un numero:"))
##B=float(input("Ingrese un numero:"))
##print(promedio(A,B))


##Ejercicio 6 F
##Definir una función que devuelva el valor absoluto de un número. (Hacerlo sin utilizar la
##función abs)


##def absoluto(numero):
##    if(numero<0):
##        numero = -numero
##    return numero
##
###Programa Principal
##n = int(input("ingrese un numero"))
##print(absoluto(n))



##Ejercicio 7 F
##a) Escribir una función con el siguiente encabezado: def exclamar(unaCadena): que
##retorne la misma cadena entre símbolos de exclamación (½!)

##def exclamar(unaCadena):
##    return "!" + unaCadena + "¡"
##cad="Programador"
##print(exclamar(cad))



##b) Escribir una función con el siguiente encabezado: def gritar(unaCadena): que
##retorne la misma cadena entre 3 símbolos de exclamación (½½½!!!)

##def gritar(unaCadena):
##    return exclamar(exclamar(exclamar(unaCadena)))
##
##cad="Programador"
##print(gritar(cad))


##Ejercicio 8 F
##a) Escribir una función que se llame elevarAlCubo que tome un número y retorne el
##valor de ese número al cubo.

##def elevarAlCubo(numero):
##    return (numero**2)
##
##n=int(input("Ingrese un numero:"))
##print(elevarAlCubo(n))

## Ejercicio 9 F
## a) Escribir una función que tome un parámetro de tipo entero y devuelva la cantidad
## de divisores positivos de ese número.



##def cantDivisores(n):
##    cont=0
##    for i in range(1,n+1):
##        if n%i==0:
##            cont=cont+1
##    return cont
##n=10
##print(cantDivisores(n))




##b) Escribir una función que tome un parámetro de tipo entero y devuelva el valor True
##si se la llama con un número primo y False en caso contrario.

##def cantDivisores(n):
##    cont=0
##    for i in range(1,n+1):
##        if n%i==0:
##            cont=cont+1
##    return cont


##def esPrimo(n):
##    if cantDivisores(n)==2:
##        return True
##    return False
##n=int(input("Ingrese un numero:"))
##if esPrimo(n):
##    print("True")
##else:
##    print("False")



##d) Hacer una función (no pura) que reciba un entero e imprima sus factores primos.
##Por ejemplo para a = 20 la función debe mostrar 2 y 5.
##Nota: Los números primos son aquellos cuyos únicos divisores positivos son ellos
##mismos y el 1.



##def esPrimo(n):
##    for i in range(2,n):
##        if n%i==0:
##            return False
##    return True

##def factPrimos(n):
##    for i in range(2,n+1):
##        if n%i==0 and esPrimo(i):
##            print(i,end=" ")
##
##
##n=int(input("ingrese un numero"))
##
##factPrimos(n)



##Ejercicio 10
##a) Hacer una función que reciba dos enteros y retorne el mayor.
##b) Hacer una función que reciba tres enteros y retorne el mayor.

##def mayorDeDos(a,b):
##    if a > b:
##        return a
##    else:
##        return b
##
##a=int(input("Ingrese un numero:"))
##b=int(input("Ingrese un numero:"))
##print("El mayor de:",a,"y",b,"es:",mayorDeDos(a,b))



#b


##def mayorDeTres(a,b,c):
##    if a > b and a > c:
##        return a
##    else:
##        if b > a and b > c:
##            return b
##        else:
##            return c
##
##a=int(input("Ingrese un numero:"))
##b=int(input("Ingrese un numero:"))
##c=int(input("Ingrese un numero:"))
##print(mayorDeTres(a,b,c))



##Ejercicio 11
##Hacer una función potencia, que reciba dos enteros a y b y retorne a**b

##def potencia(a,b):
##    resultado=a**b
##    return resultado
##
##a=int(input("Ingrese un numero:"))
##b=int(input("Ingrese un numero:"))
##print(potencia(a,b))



##Ejercicio 12
##a) Hacer una función que sume los divisores propios de un número.


##def sumaDivPropios(n):
##    suma=0
##    for i in range(1,n+1):
##        if n%i==0:
##            suma=suma+i
##    return suma
##n=int(input("Ingrese un numero:"))
##print("La suma de los divisores propios de:",n,"es:",sumaDivPropios(n))



##b) Hacer una función que indique si un número es perfecto. Número perfecto: a es
##perfecto si la suma de sus divisores propios es igual a a.


##def sumaDivPropios(n):
##    suma=0
##    for i in range(1,n):
##        if n%i==0:
##            suma=suma+i
##    return suma
##n=int(input("Ingrese un numero:"))
##if sumaDivPropios(n)==n:
##    print(n,"ES perfecto")
##else:
##    print(n,"No es perfecto")


##c) Hacer una función que determine si un número ingresado por el usuario es un número
##abundante. Número abundante: todo número natural que cumple que la suma de sus
##divisores propios es mayor que el propio número. Por ejemplo, 12 es abundante ya
##que sus divisores son 1, 2, 3, 4 y 6 y se cumple que 1+2+3+4+6=16, que es mayor
##al propio 12.


##def sumaDivPropios(n):
##    suma=0
##    for i in range(1,n):
##        if n%i==0:
##            suma=suma+i
##    return suma
##
##n=int(input("Ingrese un numero:"))
##if sumaDivPropios(n) > n:
##    print(n,"Es abundante")
##else:
##    print(n,"No es abundante")


## Ejercicio 13
## Hacer una función que indique si un número es Poderoso: Número poderoso: todo número
## natural n que cumple que si un primo p es un divisor suyo entonces p**2 también lo es. Por
## ejemplo, el número 36 es un número poderoso ya que los únicos primos que son divisores suyos
## son 2 y 3 y se cumple que 4 y 9 también son divisores de 36


# Poderoso!
##def esPrimo(n):
##    cant=0
##    for i in range(1,n+1):
##        if (n%i==0):
##            cant=cant+1
##    if cant==2:
##        return True
##    else:
##        return False
##
##def esPoderoso(n):
##    for i in range(1,n+1):
##        if(n%i==0 and esPrimo(i) and n%(i**2)!=0):
##            return False
##    return True
##
##
##num=int(input("Ingrese un numero"))
##if esPoderoso(num):
##    print(num,"SI es poderoso")
##else:
##    print(num,"NO es poderoso")



## Ejercicio 14
## Hacer una función que indique si un número es Libre de Cuadrados: Número libre de cuadrados:
## todo número natural que cumple que en su descomposición en factores primos no aparece ningún
## factor repetido. Por ejemplo, el número 30 es un número libre de cuadrados


##def esPrimo(n):
##    for i in range(2,n+1):
##        if n%i==0:
##            return False
##    return True

##a=int(input("Ingrese un numero"))
##producto=1
##for i in range(1,a+1):
##    if(a%i==0 and esPrimo(i)):
##        producto=producto*i;
##        print(producto)
##
##if(producto==a):
##    print(a,"SI es libre de cuadrados")
##else:
##    print(a,"NO es libre de cuadrados")



## Ejercicio 16
## Hacer una función (no pura) que reciba una palabra y la imprima recuadrada por asteriscos.
## Por ejemplo si la cadena fuera sobrevivir, la función debería imprimir
## **************
## * sobrevivir *
## **************


##def recuadrada(palabra):
##    asterisco=len(palabra)+4
##    for i in range(asterisco):
##        print("*",end="")
##    print("\n*",palabra,"*")
##
##    for i in range(asterisco):
##        print("*",end="")
##a=input("Ingrese una palabra:")
##recuadrada(a)


##Ejercicio 17
## El propósito de este ejercicio es tomar el código de un ejercicio anterior y encapsular una
## parte de él en un función que toma parámetros. Partiendo de la resolución del ejercicio 25 de la
## práctica de ciclos y cadenas,
## a) escribir una función que tome como parámetros una cadena y una letra, y retorne
## la cantidad de veces que aparece esa letra en esa cadena.

#b) probarla para asegurarse que funciona bien.

##c) transformar el código del ejercicio 25 para que utilice la nueva función

##def cantApariciones(letra,cadena):
##    cont=0
##    for char in cadena:
##        if char == letra:
##            cont=cont+1
##    return cont
##letra=input("Ingrese un letra:")
##cadena=input("Ingrese una cadena:")
##print("La letra",letra,"aparece en",cadena,":",cantApariciones(letra,cadena),"veces")


## Ejercicio 18 F
## Escribir una función (y probarla en un programa) para cada una de las siguientes descripciones:
## a) una función que se llame tieneRepetidas que tome una cadena como parámetro y
## devuelva True si esa cadena tiene alguna letra que aparece más de una vez y False
## en caso contrario

##def cantApariciones(letra,cadena):
##    cont=0
##    for char in cadena:
##        if char == letra:
##            cont=cont+1
##    return cont
##
##
##def tieneRepetidas(cadena):
##    for char in cadena:
##        if cantApariciones(char,cadena) > 1:
##            return True
##
##    return False
##
##cadena=input("Ingrese una cadena:")
##if tieneRepetidas(cadena):
##    print(cadena,"tiene repetidas")
##else:
##    print(cadena,"no tiene repetidas")


## b) una función que se llame aparece que tome dos parámetros, una letra y una cadena,
## y devuelva True si la letra aparece en la cadena y False en caso contrario


##def aparece(letra,cadena):
##    for char in cadena:
##        if char == letra:
##            return True
##    return False
##
##letra=input("Ingrese una letra:")
##cadena=input("Ingrese una cadena:")
##if aparece(letra,cadena):
##    print("Aparece")
##else:
##    print("No aparece")
##

## c) una función que se llame dameRepetida que tome una cadena como parámetro y
## retorne la primer letra que aparece repetida en la cadena

##def cantRepetidas(letra,cadena):
##    cont=0
##    for char in cadena:
##        if char==letra:
##            cont=cont+1
##    return cont
##
##def dameRepetida(cadena):
##    repetida=""
##    for char in cadena:
##        if cantRepetidas(char,cadena)>1:
##            repetida=char
##    return repetida
##
##cadena="Programador"
##print(dameRepetida(cadena))



## d) una función que se llame quitarRepeticiones que tome dos parámetros, una
## cadena y una letra, y devuelva otra cadena igual a la anterior pero sin las
## repeticiones de esa letra. Por ejemplo, un programa que llame a la función
## así: quitarRepeticiones(mate cocido, c), deverá retornar la cadena mate
## coido.


##def aparece(letra,cadena):
##    for char in cadena:
##        if char == letra:
##            return True
##    return False
##
##def quitarRepeticiones(letra,cadena):
##    sinRepetidas=""
##    for char in cadena:
##        if char == letra:
##            if not aparece(letra,sinRepetidas):
##                sinRepetidas=sinRepetidas+char
##        else:
##            sinRepetidas=sinRepetidas+char
##    return sinRepetidas
##
##letra="c"
##cadena="mate cocido"
##print(quitarRepeticiones(letra,cadena))




## Ejercicio 19 F
## Se desea automatizar el cálculo de la tarifa telefónica para una lista de clientes. La empresa
## informa que cada llamado tiene un costo por conexión más un costo por el tiempo consumido
## en segundos. Se cuenta con las siguientes funciones ya implementadas.

## ObtenerCantidadLlamados(nroCliente): retorna la cantidad de llamados para un cliente.   :::
## ObtenerTiempoPorLlamada(nroCliente, nroLlamada): retorna la cantidad de segundos de un llamado de un cliente.
## ObtenerCostoPorLlamada(): retorna el costo fijo por cada llamada.                 :::
## ObtenerCostoPorTiempo(seg): retorna el costo de una llamada que dura seg segundos.

## Realizar un programa que indique el monto de la factura para cada cliente. Además, el sistema
## registra los clientes en una base para promociones, con el siguiente comportamiento. Los clientes
## que ya estaban en la base, se los da de baja para evitar volver a ofrecer dos veces seguidas
## la promoción. Si el tiempo total de comunicaciones para un cliente supera las dos horas, se lo
## agrega a la base para ofrecerle la promoción, salvo los dados de baja previamente. Para ello se
## cuenta con las siguientes funciones ya implementadas.

## Esta(nroCliente): indica si el cliente está en la base de promociones.
## Alta(nroCliente): agrega el cliente a la base.
## Baja(nroCliente): da de baja al cliente en el registro de promociones.

def tarifaTelefonica(listaClientes):
    costoPorLlamada=ObtenerCantidadLlamados(nroCliente)*ObtenerCostoPorLlamada()

##

















