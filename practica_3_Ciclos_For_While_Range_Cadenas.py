##Realizar un programa que solicite dos números y realice la división entre ellos, no se debe permitir que el denominador sea 0.

##Realizar un programa que imprima la tabla del 2 (desde el 1 al 10).

##Modificar el programa anterior, para que pida al usuario un número entero e imprima la tabla de multiplicar de dicho número.

##Realizar un programa que sume los primeros n números naturales. (n lo indica el usuario)

##Realizar un programa que sume los primeros números impares hasta n. (n lo indica el usuario)

##Realizar un programa que sume los primeros n números impares. (n lo indica el usuario)


# 1
##numerador=float(input("Ingrese un numero:"))
##denominador=float(input("Ingrese un numero:"))
##while denominador==0:
##    denominador=float(input("Ingrese un numero distinto de ¡0!:"))
##division=(numerador/denominador)
##print(division)

# 2

##cont=1
##while cont <=10:
##    print(2,"x",cont,"=",2*cont)
##    cont=cont+1

# 3

##n=int(input("Que tabla desea calcular:"))
##cont=1
##while cont<=10:
##    print(n,"x",cont,"=",n*cont)
##    cont=cont+1


# 4

##n=int(input("Ingrese un numero:"))
##suma=0
##cont=1
##while cont<=n:
##    suma=suma+cont
##    cont=cont+1
##print("La suma de los primeros",n,"naturales es:",suma)



#suma primeros numeros impares hasta n
##n=int(input("ingrese un numero: "))
##i=1
##suma=0
##while(i<=n):
##    suma=suma+i
##    print(i,suma)
##    i=i+2

##n=int(input("ingrese un numero: "))
##cont=1
##suma=0
##impares=1
##while cont<=n:
##    suma=suma+impares
##    impares=impares+2
##    print(cont,impares,suma)
##    cont=cont+1



# Ciclos for
#1
#Realizar un programa que imprima la tabla del número que el usuario desee (desde el 1 al 10). Hacer ahora una versión con ciclos for.

##n=int(input("Ingrese un numero:"))
##for i in range(1,10+1):
##    print(n,"x",i,"=",n*i)

# 2
##Escribir un programa que le pregunte al usuario un número entero positivo N, y que calcule su factorial ( N! )
##	(ej: 5!=5*4*3*2*1)

##N=int(input("Ingrese un entero positivo:"))
##factorial=1
##for i in range(1,N+1):
##    factorial=factorial*i
##    print(i,factorial)

# 3
##Escribir un programa que le pida al usuario dos números. Devuelve el primer número elevado al segundo. ()

##n=int(input("Ingrese un numero:"))
##m=int(input("Ingrese un numero:"))
##print(m**2)

## 4
##Escribir un programa que le pida al usuario números (la cantidad que el usuario desee) y calcule el promedio

##cantidad=int(input("Ingrese la cantidad de numeros:"))
##suma=0
##for i in range(1,cantidad+1):
##    numero=int(input("Ingrese numeros:"))
##    suma=suma+numero
##print(suma/cantidad)


## 5
##Escribir un programa que le pregunte al usuario un número entero positivo n y que calcule la parte entera de

##import math
##print ("Este programa calcula parte entera de la raiz cuadrada")
##n=int(input("Ingrese un numero"))
##i=1
##while(i*i<=n):
##    i=i+1
##
##print("La parte entera de la raiz cuadrada de",n,"es: ",i-1)
##
##if(int(math.sqrt(n))==i-1):
##    print("Bien resuelto")
##else:
##    print("ERROR"


##(solo para ingeniosos) Escribir un programa que le pregunte al usuario un número entero positivo N, y que
##muestre por pantalla la cantidad de cifras que tiene. (Ej: 1492 tiene 4 cifras)


##print ("Este programa calcula la cantidad de cifras de un numero")
##n=int(input("Ingrese un numero"))
##if n==0:
##    print("El numero tiene 1 cifra")
##else:
##    if n<0:
##        n=n*(-1)
##    cont=0
##    while(n>=1):
##        n=n/10
##        cont=cont+1
##    print("El numero tiene",cont,"cifras")


##n=int(input("Ingrese un numero"))
##cantCifras=len(str(n))
##print(n,"Tiene:",cantCifras,"cifras")



# Pracica 3

##Ejercicio 1 F
##a) Hacer un programa que muestre, mediante un ciclo, los primeros 5 números naturales
##(1, 2, 3, 4 y 5).
##b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
##primeros n números naturales (1, 2, · · · , n).

##inicio=1
##while inicio<=5:
##    print(inicio,end="")
##    inicio=inicio+1


##for i in range(1,5+1):
##    print(i,end=",")

#b
##n=int(input("Ingrese un numero:"))
##for i in range(1,n+1):
##    print(i,end=",")


##Ejercicio 2 F
##a) Hacer un programa que muestre, mediante un ciclo, los números desde el 4 hasta el
##   7  (4, 5, 6 y 7).
##b) Hacer un programa que permita al usuario elegir un número m y un n y luego
##muestre todos los naturales entre m y n (m, m + 1, m + 2, · · · , n − 1, n). ¾Qué pasa
##si n es menor que m?

##inicio=4
##while inicio<=7:
##    print(inicio,end=",")
##    inicio=inicio+1


##m=int(input("Ingrese un numero:"))
##n=int(input("Ingrese un numero:"))
##inicio=m
##while inicio<=n:
##    print(inicio,end=",")
##    inicio=inicio+1


## Ejercicio 3 F
## a) Hacer un programa que muestre, mediante un ciclo, los 5 números naturales que le
## siguen al 10 (11, 12, · · · , 15).
## b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
## 5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).
## c) Hacer un programa que permita al usuario elegir un número n y un número c, y
## luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).


##inicio=10
##while inicio<=15:
##    print(inicio,end=",")
##    inicio=inicio+1


##n=int(input("Ingrese un numero:"))
##inicio=n
##fin=n+5
##while inicio<=fin:
##    print(inicio,end=",")
##    inicio=inicio+1


##n=int(input("Ingrese un numero:"))
##c=int(input("Ingrese un numero:"))

##inicio=n
##fin=c
##while inicio<=fin:
##    print(inicio,end=",")
##    inicio=inicio+1


##n=int(input("Ingrese un numero:"))
##c=int(input("Ingrese un numero:"))
##for i in range(n,c+1):
##    print(i,end=",")



##Ejercicio 4 F
##a) Hacer un programa que muestre, mediante un ciclo, los números desde el 5 hasta el
##11 salteando de a 2 elementos (5, 7, 9 y 11)
##b) Hacer un programa que permita al usuario elegir un número m y un n y luego
##muestre todos los naturales entre m y n, pero salteando de a 3. Por ejemplo, si el
##usuario ingresara un n igual a 2 y un m igual a 14, el programa deberá mostrar
##2, 5, 8, 11, 14.
##c) Hacer un programa que permita al usuario elegir un número n, un m y un p y
##luego muestre todos los naturales entre m y n, pero salteando de a p números. Por
##ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4,
##el programa deberá mostrar 2, 6, 10, 14.


##inicio=5
##fin=11
##while inicio<=fin:
##    print(inicio,end=",")
##    inicio=inicio+2



##Ejercicio 8

##a) Hacer un programa que reciba un número n y muestre todas las potencias de 2
##menores a n. Por ejemplo, si el usuario ingresa 20, el programa mostrará: 1 2 4 8
##16. Ayuda: pensar primero si sería más práctico utilizar la sentencia while o for.

##b) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
##potencias de 2. Por ejemplo, si el usuario ingresa 6, el programa mostrará: 1 2 4 8
##16 32.

##c) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
##potencias de n. Por ejemplo, si el usuario ingresa 4, el programa mostrará: 1 4 27
##256. Es decir, 1**1 2**2 3**3 4**4

#a)

##n=int(input("Ingrese un numero:"))
##inicio=1
##while inicio<=n:
##    print(inicio)
##    inicio=inicio*2


#b)

##n=int(input("Ingrese un numero:"))
##potencia=1
##cont=1
##while cont<=n:
##    print(potencia)
##    potencia=potencia*2
##    cont=cont+1


# c

##n=int(input("Ingrese un numero:"))
##potencia=1
##inicio=1
##while inicio<=n:
##    print(potencia**potencia)
##    potencia=potencia+1
##    inicio=inicio+1


##Ejercicio 9
##a) Hacer un programa que permita al usuario elegir un número positivo n y luego
##muestre en pantalla todos los divisores de n

##n=int(input("Ingrese un numero:"))
##for i in range(1,n+1):
##    if n%i==0:
##        print(i)

##b) Hacer un programa que permita al usuario elegir un número positivo n y luego
##muestre en pantalla todos los divisores pares de n.

##n=int(input("Ingrese un numero:"))
##for i in range(1,n+1):
##    if n%i==0 and i%2==0:
##        print(i)

##n=int(input("Ingrese un numero:"))
##cont=1
##while cont<=n:
##    if n%cont==0 and cont%2==0:
##        print(cont,end=",")
##    cont=cont+1



##c) Hacer un programa que permita al usuario elegir un número positivo n y luego
##muestre en pantalla la cantidad de divisores de n


##n=int(input("Ingrese un numero:"))
##cant=0
##for i in range(1,n+1):
##    if n%i==0:
##        cant=cant+1
##print("La cantidad de divisores de",n,"es:",cant)



##d) Hacer un programa que permita al usuario elegir un número positivo n y luego
##muestre en pantalla la suma de los divisores de n.

##n=int(input("Ingrese un numero:"))
##suma=0
##for i in range(1,n+1):
##    if n%i==0:
##        suma=suma+i
##print("La suma de los divisores de",n,"es",suma)

##e) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
##muestre en pantalla los primeros c divisores de n


##n=int(input("Ingrese un numero:"))
##c=int(input("Ingrese un numero:"))
##k=0
##i=1
##while k<c and i<=n:
##    if n%i==0:
##        k=k+1
##        print (k,"- divisor de ",n,"es ",i)
##    i=i+1
##if k<c:
##    print("No hay mas divisores")


##f) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
##muestre en pantalla los últimos c divisores de n


##n=int(input("Ingrese un numero:"))
##c=int(input("Ingrese un numero:"))
##k=0
##i=1


##Ejercicio 10
##Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en
##pantalla el producto (es decir, la multiplicación) de los numeros entre 1 y n.

##n=int(input("Ingrese un numero:"))
##cont=1
##producto=1
##while cont<=n:
##    producto=producto*cont
##    cont=cont+1
##    print(producto)


##Ejercicio 11
##Hacer un programa que reciba un número m y determine el primer n para el cual la suma
##1+2+...+n > m. Por ejemplo, si el usuario ingresa 11 se deberá retornar 5 ya que 1+2+3+4 =
##10 < 11 y 1 + 2 + 3 + 4 + 5 = 15 > 11

##m=int(input("Ingrese un numero:"))
##suma=0
##i=0
##while suma<=m:
##    i=i+1
##    suma=suma+i
##print("El primer n para el cual la suma supera a",m,"es",i)





##Ejercicio 12
##a) Hacer un programa que permita al usuario elegir un número positivo n y luego
##muestre en pantalla los n primeros términos de la sucesión an = 2n. Es decir 2, 4,
##6...


##n=int(input("Ingrese un numero:"))
##for i in range(1,n+1):
##    sucesion=2*i
##    print(sucesion,end=", ")


##b) Idem anterior para la sucesión an = 2n − 1.

##n=int(input("Ingrese un numero:"))
##for i in range(1,n+1):
##    sucesion=(2*i)-1
##    print(sucesion,end=", ")


##c) Idem anterior para la sucesión an = n**2

##n=int(input("Ingrese un numero:"))
##for i in range(1,n+1):
##    sucesion=i**2
##    print(sucesion,end=", ")


##d) Idem anterior para la sucesión an = n**3 − n**2

##n=int(input("Ingrese un numero:"))
##for i in range(1,n+1):
##    sucesion=(i**3) - (i**2)
##    print(sucesion,end=", ")


##e) Idem anterior para la sucesión an =1/n**2


##n=int(input("Ingrese un numero:"))
##for i in range(1,n+1):
##    sucesion= 1/i**2
##    print(sucesion,end=", ")

##Ejercicio 13
##a) Hacer un programa que permita al usuario elegir un número positivo n y luego
##muestre en pantalla las n primeras sumas parciales de la sucesión an = 2n. Es decir,
##2 6 12 20...

##n=int(input("Ingrese un numero:"))
##suma=0
##for i in range(1,n+1):
##    suma=suma+2*i
##    print(suma,end=", ")

##b) Idem anterior para la sucesión an = n**2

##n=int(input("Ingrese un numero:"))
##for i in range(1,n+1):
##    suma=suma+i**2
##    print(suma,end=", ")


##Ejercicio 14 F
##El logaritmo natural de 2 (ln(2)) se puede aproximar de la siguiente manera:
##ln(2) = 1 − 1/2 + 1/3 − 1/4 + 1/5

##n=int(input("Ingrese un numero:"))
##suma=0
##for i in range(1,n+1):
##    if i%2!=0:
##        suma=suma+1/i
##    else:
##        suma=suma-1/i
##print("La suma de los",n,"terminos es:",suma)


## Ejercicio 15 F
## El número 1/4 π se puede aproximar de la siguiente manera: 1/4π =
## 1 − 1/3 + 1/5 − 1/7 + 1/9 − 1/11 + 1/13 − 1/15

##n=int(input("Ingrese un numero:"))
##suma=0
##signo=1
##var=1
##for i in range(1,n+1):
##    suma=suma+signo*(1/var)
##    var=var+2
##    signo=signo*-1
##print(suma)




##Ejercicio 16 F
##Escribir un programa que solicite al usuario un número positivo y aproxime
##el valor del número e de la siguiente manera: (ejemplo para 7 términos)
#1/0!+1/1!+1/2!+1/3!+1/4!+1/5!+1/6!

##n=int(input("Ingrese un numero:"))
##suma=1
##factorial=1
##for i in range(1,n):
##    factorial=factorial*i
##    suma=suma+1/factorial
##print(suma)



##Ejercicio 17
##a) Hacer un programa que permita al usuario elegir un número m y un n y muestre
##pares de numeros complementarios, o sea (m, n)(m + 1, n − 1)(m + 2, n − 2). . .(n −
##1, m + 1)(n, m). Por ejemplo, el usuario ingresa 5 y 10, 5 será el complementario de
##10, 6 el de 9 y 7 el de 8, y deberá mostrarse:
## 5 10
## 6 9
## 7 8
## 8 7
## 9 6
## 10 5

##m=int(input("Ingrese un numero:"))
##n=int(input("Ingrese un numero:"))
##
##aux=n
##cont=m
##while cont<=n:
##    print(cont,aux)
##    aux=aux-1
##    cont=cont+1



##Ejercicio 18 F ♣
##a) Escribir un programa que permita al usuario elegir un número m y un n y muestre
##todos los pares de numeros que se pueden formar con los números que están entre
##ellos. Por ej. si el usuario ingresara 4 y 6, el programa deberá mostrar
## 4 4
## 4 5
## 4 6
## 5 4
## 5 5
## 5 6
## 6 4
## 6 5
## 6 6


##m=int(input("Ingrese un numero:"))
##n=int(input("Ingrese un numero:"))
##for i in range(m,n+1):
##    for j in range(m,n+1):
##        print(i,j)




##Ejercicio 19 ♣
##a) Escribir un programa que permita al usuario elegir un número m y un n y muestre
##todos los pares de numeros que se pueden formar con los números que están entre
##ellos, pero esta vez que lo haga sin repetir inversos. Por ej. si el usuario ingresara 4
##y 6, el programa deberá mostrar
##4 4
##4 5
##4 6
##5 5
##5 6
##6 6


##m=int(input("Ingrese un numero:"))
##n=int(input("Ingrese un numero:"))
##
##for i in range(m,n+1):
##    for j in range(i,n+1):
##        print(i,j)



## Ejercicio 20 F
## Hacer un programa que simule el juego de la quiniela. El usuario debe elegir un número del
## 0 al 99 y un monto a apostar, si acierta el número gana 70 veces lo apostado. (El número de la
## suerte debe ser elegido al azar)

##import random
##
##numero=int(input("Ingrese un numero:"))
##monto=float(input("Ingrese su monto a apostar:"))
##aleatorio=random.randint(1,99)
##print(aleatorio)
##if numero==aleatorio:
##    gana=True
##else:
##    gana=False
##
##if gana:
##    print("Usted gano:",monto*70)
##else:
##    print("Gracis por participar")


## Ejercicio 21 F
## Hacer un programa que permita al usuario jugar al piedra, papel o tijera contra
## la computadora. Se debe jugar al mejor de 5, es decir, si uno de los participantes
## consigue 3 victorias el juego termina.

##import random
##
##piedra = 0
##papel = 1
##tijera = 2
##
##seguirJugando = True
##while(seguirJugando):
##
##    print("Piedra Papel Tijera")
##    print("Seleccione una opcion valida")
##    print("0 ) Piedra\n")
##    print("1 ) Papel\n")
##    print("2 ) Tijera\n")
##
##    opcion = int(input("Piedra Papel Tijera\n Ingrese Opcion:\n 0 ) Piedra\n 1 ) Papel\n 2 ) Tijera\n"))
##
##    opcionPC = random.randrange(0,3,1)
##
##    if(opcion == piedra):
##
##        if(opcionPC == piedra):
##            print("Vos elegiste piedra y yo tambien")
##            print("Empatamos")
##        else:
##            if(opcionPC == papel):
##                print("Vos elegiste piedra y yo papel")
##                print("Gane yo !!")
##            else:
##                if(opcionPC == tijera):
##                    print("Vos elegiste piedra y yo tijera")
##                    print("Ganaste vos !!")
##    else:
##        if(opcion == papel):
##            if(opcionPC == piedra):
##                print("Vos elegiste papel y yo piedra")
##                print("Ganaste vos !!")
##            else:
##                if(opcionPC == papel):
##                    print("Vos elegiste papel y yo papel")
##                    print("Empatamos")
##                else:
##                    if(opcionPC == tijera):
##                        print("Vos elegiste papel y yo tijera")
##                        print("Gane yo !!")
##        else:# if(opcion == tijera):
##            if(opcionPC == piedra):
##                print("Vos elegiste tijera y yo piedra")
##                print("Gane yo !!")
##            else:
##                if(opcionPC == papel):
##                    print("Vos elegiste tijera y yo papel")
##                    print("Ganaste vos !!")
##                else:
##                    if(opcionPC == tijera):
##                        print("Vos elegiste tijera y yo tijera")
##                        print("Empatamos")
##
##    print("Presiona 1 para salir y cualquier otra para seguir jugando\n")
##    respuesta = int(input("Presiona 1 para salir y cualquier otra para seguir jugando\n"))
##    if(respuesta == 1):
##        seguirJugando = False
##
##print("Juego Finalizado")




##Ejercicio 22 F
##¾Para qué números enteros distintos de cero es cierto que A + B + C = A x B x C ? (lo
##curioso es que sólo hay una solución)

##a=int(input("Ingrese un numero !=0: "))
##b=int(input("Ingrese un numero !=0: "))
##c=int(input("Ingrese un numero !=0: "))
##if (a+b+c) == (a*b*c):
##    print("Es cierto para A=",A,"B=",b,"C=",c)
##else:
##    print("a+b+c no es igual que a*b*c")




# CADENAS ACTVIDADES
##1. Hacer un programa que dada una cadena ingresada por el usuario indique la cantidad de apariciones de la letra “a”.

##cadena=input("Ingrese una palabra:")
##cont=0
##for char in cadena:
##    if char=="a":
##        cont=cont+1
##print("La letra a aparece:",cont,"veces")

##2. Hacer un programa que dada una cadena ingresada por el usuario indique la cantidad de vocales

##cadena=input("Ingrese una palabra:")
##cont=0
##for char in cadena:
##    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
##        cont=cont+1
##print("La cantidad de vocales que tiene la palabra:",cadena,"es:",cont)


##3. Hacer un programa que dados un caracter y una cadena indique la cantidad de apariciones de dicho caracter en la cadena.

##cadena=input("Ingrese una cadena:")
##caracter=input("Ingrese un caracter:")
##cont=0
##for char in cadena:
##    if caracter == char:
##        cont=cont+1
##print(cont)






##4. Hacer un programa que dados un caracter y una cadena muestre la misma
##   cadena con un * en lugar de dicho carácter.
##	Ejemplo: 	programador 		r
##				p*og*amado*


##cadena="Programador"
##caracter="r"
##nuevaCadena=""
##for char in cadena:
##    if char == caracter:
##        nuevaCadena=nuevaCadena+"*"
##    else:
##        nuevaCadena=nuevaCadena+char
##print(nuevaCadena)




##Como ejercicio, escribí un programa que tome una cadena como parámetro y que imprima
##solo las consonantes de la cadena, en líneas separadas

##cadena="Programador"
##for char in cadena:
##    if char != "o" and char != "a":
##        print(char)



## Parte 2  Cadenas
## Ejercicio 23 F
## a) Escribir un programa que pida al usuario un número n y muestre una línea de n
## asteriscos. Ejemplo, para n = 8, el programa deberá mostrar:
## ********

##n=8
##for i in range(1,n+1):
##    print("*",end="")


##n=8
##cont=1
##while cont<=n:
##    print("*",end="")
##    cont=cont+1


##b) Escribir un programa que pida al usuario un número n y muestre n líneas de
##1, 2, 3, ...n asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá
##mostrar:
##*
##**
##***
##****
##*****

##n=5
##cont=1
##nueva=""
##while cont<=n:
##    nueva=nueva+"*"
##    print(nueva)
##    cont=cont+1


##n=5
##nueva=""
##for i in range(1,n+1):
##    nueva=nueva+"*"
##    print(nueva)



## c)Escribir un programa que pida al usuario un número n y muestre n líneas de 2n − 1
## asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá mostrar:
## *
## ***
## *****
## *******
## *********


##n=5
##asterisco="*"
##
##for i in range(1,n+1):
##    salida=2*i-1
##    print(salida*asterisco)



##Ejercicio 24 F
##a) Sabiendo que la pantalla de la consola tiene 80 caracteres de ancho, hacer un
##   programa que, dada una palabra, la escriba en el centro de la pantalla.
##b) Hacer una programa que, dada una palabra, la escriba pegada a la derecha de la
##   pantalla.


##cadena = input("ingrese una cadena")
##nuevaCadena=""
##ancho=80-len(cadena)
##mitad=ancho//2
##nuevaCadena=nuevaCadena+(" "*mitad)
##nuevaCadena=nuevaCadena+cadena
##nuevaCadena=nuevaCadena+(" "*mitad)
##print(nuevaCadena)


## b

##cadena = input("ingrese una cadena")
##nuevaCadena=""
##pegada_Derecha=80-len(cadena)
##nuevaCadena=nuevaCadena+(" "*pegada_Derecha)
##nuevaCadena=nuevaCadena+cadena
##print(nuevaCadena)



## Ejercicio 25 F
## Hacer una programa que, dada una palabra, la escriba recuadrada por asteriscos. Por ejemplo,
## si la palabra es "Ganaste", el programa debería escribir:
## ***********
## * Ganaste *
## ***********


##palabra=input("Ingrese una palabra:")
##asterisco=len(palabra)+4
##print(asterisco*"*")
##print("*",palabra,"*")
##print(asterisco*"*")


##Ejercicio 26
##Hacer un programa que dada una palabra y una letra, imprima la cantidad de apariciones de
##esa letra.


##palabra=input("Ingrese una palabra:")
##letra=input("Ingrese un letra:")
##cont=0
##for char in palabra:
##    if char==letra:
##        cont=cont+1
##print(cont)



##Ejercicio 27
##Escribir un programa que pida al usuario una cadena e indique si esta posee un
##diptongo (dos vocales unidas).





## Ejercicio 28
## Escribir un programa que pida al usuario una cadena y una letra y reemplace las apariciones
## de dicha letra por asteriscos. Por ejemplo, si el usuario ingresa:
## "programador"
## "r"
## el programa debe devolver "p*og*amado*"

##cadena="Programador"
##letra="r"
##nueva=""
##for char in cadena:
##    if char==letra:
##        nueva=nueva+"*"
##    else:
##        nueva=nueva+char
##print("cadena vieja:",cadena)
##print("cadena nueva:",nueva)






## Ejercicio 29
## Hacer un programa que genere una clave provisoria para la gestión online de clientes de una
## empresa. El programa le pedirá el apellido y generará una clave de 5 caracteres, tomará las
## primeras 4 consonantes de la palabra ingresada. Cuando las consonantes no alcancen a 4, las
## faltantes las reemplazará por "*". Ejemplos:
## clemente CLMN
## rivera RVR*
## oreo R***
## La clave se completará con 1 dígito generado aleatoriamente entre 0 y 9.
## Ejemplos: CLMN1 RVR*4 R***7


##import random
##apellido=input("Ingrese su apellido:")
##clave=""
##aleatorio=random.randrange(0,9)
##for char in apellido:
##    if len(clave) < 4 and char !="a" and char !="e" and char !="i" and char !="o" and char !="u":
##        clave=clave+char
##while len(clave)<4:
##    clave=clave+"*"
##clave=clave+str(aleatorio)
##
##print(clave)


#

##Ejercicio 30
##Hacer un programa que solicite dos cadenas, nombre y apellido y arme el legajo de estudiantes
##de la universidad de la siguiente manera:
##Los 3 primeros números del legajo coinciden con los primeros del dni luego "_", luego las 3
##primeras letras del apellido y por ultimo la primera y ultima del nombre.
##Por ejemplo:
##Javier Rodriguez 38946702
##Legajo: 389_rodjr
##nombre = input("Ingrese un nombre")
##apellido = input("ingrese un apellido")
##dni = input("Ingrese un DNI")

##
##dni=input("Ingrese un DNI:")
##nombre=input("Ingrese un nombre:")
##apellido=input("Ingrese un apellido:")
##
##legajo=""
##
##for numero in dni:
##    if len(legajo) <3:
##        legajo=legajo+(numero)
##legajo=legajo+"_"
##cont=0
##for char in apellido:
##    if cont < 3:
##        legajo=legajo+char
##        cont=cont+1
##
##cont=0
##for char in nombre:
##    if cont==0:
##        legajo=legajo+char
##    if cont == len(nombre)-1:
##        legajo=legajo+char
##    cont=cont+1
##print(legajo)
##
































