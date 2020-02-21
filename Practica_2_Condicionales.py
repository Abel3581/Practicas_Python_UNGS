##Practica 2 Condicionales if else

##1. Dado un número indicar si es par o impar.
##2. Hacer un programa que solicite dos números e indique el signo de la multiplicación sin efectuarla.
##3. Introducir dos números enteros por el teclado, DIVIDENDO y DIVISOR. Si dividendo es divisible por divisor,
##   el programa ha de mostrar el mensaje “DIVISIBLES”.
##4. Dadas las notas de tres parciales. Indicar si promociona, va a final o recursa (sabiendo que se Aprueba con
##   un promedio mayor o igual a 7, se va a Final con un promedio menor a 7 y mayor o igual a 4 y con menos de 4 Recursa.)


#1

##numero=int(input("Ingrese un numero:"))
##if numero % 2==0:
##    print(numero,"Es par")
##else:
##    print(numero,"Es impar")

#2

##n=float(input("Ingrese un numero:"))
##m=float(input("Ingrese un numero:"))
##print(n,"*",m)

#3
##dividendo=int(input("Ingrese un numero:"))
##divisor=int(input("Ingrese un numero:"))
##if divisor!=0:
##    print(dividendo,"ES divisible por:",divisor)
##else:
##    print(dividendo,"No se puede dividir por:",divisor)



#4

##nota1=float(input("Ingrese su nota:"))
##nota2=float(input("Ingrese su nota:"))
##nota3=float(input("Ingrese su nota:"))
##promedio=(nota1+nota2+nota3)/3
##
##if promedio >= 7:
##    print("Promocionado")
##else:
##    if promedio  >=4 and promedio <7:
##        print("Va a final")
##    else:
##        print("Recursa")


##Ejercicio 2
##Un ciudadano argentino está exento de votar en estos casos:
##Tiene más de 70 años
##Tiene entre 18 y 70 años pero se encuentra a más de 500 km del centro de votación.
##Suponiendo que las variables edad y distancia representan la edad y la distancia del ciudadano, escribir la expresión lógica que representa esta situación.

##edad=int(input("Ingrese su edad:"))
##distancia=float(input("Ingrese a cuantos kilometros vive del centro de votacion:"))
##if distancia <500 and edad >=18 and edad <=70:
##    print("OBLIGADO A VOTAR")
##else:
##    print("EXENTO DE VOTAR")

##Ejercicio 5
##Escribir en papel un programa que pida una nota y que en el caso de que sea menor a cuatro
##muestre Debe recuperar. Luego pasarlo a Python.


##nota=float(input("Ingrese una nota:"))
##if nota <4:
##    print("Debe recuperar")
##else:
##    print("Aprobado...")




##Ejercicio 6
##a) Escribir en papel un programa que pida al usuario dos números, y que muestre en
##pantalla al mayor de ambos. Luego hacer 3 corridas de escritorio, luego pasarlo a
##Python y por último correr el programa con los valores iniciales de las corridas y
##vericar que funciona como se esperaba.
##b) Ídem anterior pero para encontrar el menor


##n1=int(input("Ingrese un numero:"))
##n2=int(input("Ingrese un numero:"))
##if n1 > n2:
##    print("El mayor es",n1)
##else:
##    print("El mayor es",n2)


##Ejercicio 7
##Escribir en papel un programa que pida al usuario dos números de punto otante y muestre
##su promedio. Además, si el promedio es mayor que 7 el programa debe mostrar en pantalla
##Aprobado y si no, debe mostrar Desaprobado. Después de hacerlo en papel, pasarlo a Python.


##n1=float(input("Ingrese un numero:"))
##n2=float(input("Ingrese un numero:"))
##promedio= (n1+n2)/2
##if promedio >7:
##    print("Aprobado")
##else:
##    print("Desaprobado")



##Ejercicio 8
##Escribir en papel un programa que tome un número entero positivo ingresado por el usuario
##y muestre por pantalla Usted ingresó un número de una sola cifra o Usted ingresó un número
##de más de una cifra según corresponda. Realizar 4 corridas de escritorio, escribirlo en Python
##y luego correrlo en la computadora con los valores iniciales de las corridas y vericar que hayan
##dado como se esperaba.

##numEntero=int(input("Ingrese un numero:"))
##if numEntero <10 and numEntero >-10:
##    print("Usted ingreso un numero de una sola cifra")
##else:
##    print("Usted ingreso un numero de mas de una cifra")



##Ejercicio 9 F
##Se tiene la siguiente lista con DNIs de personas.
##30612453
##23763290
##21448503
##34582048
##15364857
##Dado otro número de DNI cualquiera, se desea construir un programa que determine si es alguno
##de los existentes en el listado. Escribir el programa en papel y luego pasarlo a Python.


##DNI=int(input("Ingrese un DNI:"))
##if DNI == 30612453 or DNI == 23763290 or DNI == 21448503 or DNI == 34582048 or DNI == 15364857:
##    print("DNI ya se encuentra registrado")
##else:
##    print("DNI no se encuentra en la lista")



##Ejercicio 10 F
##Hacer en pseudocodigo y luego un programa que calcule el importe que se le facturará a un
##cliente por consumo de electricidad sabiendo que la compañía que se la provee cobra una tarifa
##ja de 20 pesos que incluye los primeros 200 KW consumidos y los KW excedentes se los cobra
##a 0,5 pesos el KW, además se agregan $7, 8 de impuestos. Se leen los valores del medidor al
##comienzo y al n del período.


##kw_inicial=float(input("Ingrese kw iniciales:"))
##kw_finales=float(input("Ingrese kw finales:"))
##kw=kw_inicial-kw_finales
##tarifaFija=20
##impuesto=7.8
##if kw <=200:
##    importe=tarifaFija+impuesto
##else:
##    importe= tarifaFija+impuesto+0.5*(kw -200)
##print("El precio a pagar es:",importe)




##Ejercicio 11 F
##Se desea escribir un programa que pida al usuario tres números y luego muestre el mayor de
##ellos. Escribir el programa en papel, realizar 3 pruebas de escritorio y luego pasarlo a Python y
##vericar los resutlados.

##n1=int(input("Ingrese un numero:"))
##n2=int(input("Ingrese un numero:"))
##n3=int(input("Ingrese un numero:"))
##
##if n1 > n2 and n1 >n3:
##    mayor=n1
##else:
##    if n2 > n1 and n2 > n3:
##        mayor=n2
##    else:
##        mayor=n3
##print("El mayor es:",mayor)


##Ejercicio 12
##Un profesor clasica las notas de sus alumnos de la siguiente manera:
##1-3 Reprobado
##4-6 Debe rendir examen nal
##7-10 Eximido
##a) Escribir un programa que indique la clasicación de una nota.
##b) Escribir un programa que pida 3 notas, calcule el promedio e indique la clasicación
##del mismo.


##nota1=int(input("Ingrese un numero:"))
##nota2=int(input("Ingrese un numero:"))
##nota3=int(input("Ingrese un numero:"))
##promedio=(nota1+nota2+nota3)/3
##if promedio >=7:
##    print("Eximido")
##elif promedio >=4 and promedio <=6:
##    print("Debe rendir final")
##else:
##    print("Reprobado")


##Ejercicio 13 F
##Escribir un programa que pida al usuario dos enteros y que luego muestre si el primero es
##mayor que el segundo o viceversa

##entero1=int(input("Ingrese un entero:"))
##entero2=int(input("Ingrese un entero:"))
##if entero1 > entero2:
##    print(entero1,"Es mayor que:",entero2)
##else:
##    print(entero2,"Es mayor que:",entero1)

##Ejercicio 14 F
##Escribir un programa que pida al usuario dos enteros y los guarde en dos variables. Si el
##primero de los valores fuera menor que el segundo, el programa deberá además intercambiar los
##valores de las variables y mostrarlos de mayor a menor


##a=int(input("Ingrese un numero:"))
##b=int(input("Ingrese un numero:"))
##if a>b:
##    print(a,"\n",b)
##
##else:
##    print(b,"\n",a)


##Ejercicio 15 F ♣
##Escribir un programa que pida al usuario tres enteros y los guarde en tres variables a, b y c.
##El programa deberá luego hacer que en la variable a quede el menor de los valores recibidos, en
##b el intermedio y en c el mayor (es decir, ordenará los valores).

##a=int(input("Ingrese un numero:"))
##b=int(input("Ingrese un numero:"))
##c=int(input("Ingrese un numero:"))
##
##
##print("El menor es:",menor)
##print("El del medio es:",medio)
##print("El mayor es:",mayor)































