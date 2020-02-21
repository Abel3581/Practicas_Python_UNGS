##Hacer un programa que pida el precio unitario y la cantidad de productos adquiridos y calcule el precio final.

##cantProductos=int(input("Ingrese la cantidad de productos:"))
##precioProducto=float(input("Ingrese el precio por unidad:"))
##precioFinal=cantProductos*precioProducto
##print("El precio final es:",precioFinal)


##Hacer un programa que dadas tres notas parciales A,B,C y calcule el promedio.

##A=float(input("Ingrese una nota:"))
##B=float(input("Ingrese una nota:"))
##C=float(input("Ingrese una nota:"))
##promedio=(A+B+C)/3
##print("El promedio es:",promedio)

##Hacer un programa que pida el radio R de una circunferencia, y calcule la longitud y el área. Longitud=2R    Área=R2
##radio=float(input("Ingrese el radio de la circunferencia:"))
##longitud=(6.28)*radio
##area=(3.14)*radio**2
##print("Longitud:",longitud,"\nArea:",area)

## 3
##Escribir en papel un programa que pida al usuario dos valores cualquiera e imprima en pantalla la
##suma de ambos.
##
##val1=int(input("Ingrese un valor:"))
##valor2=int(input("Ingrese otro valor:"))
##suma=val1+valor2
##print("La suma es:",suma)


## 4
##Escribir en papel un programa que pida al usuario un valor entero y devuelva el siguiente número
##más grande

##valor=int(input("Ingrese un valor:"))
##print(valor+1)

## 5   PROMEDIO
##a=float(input("Ingrese un valor:"))
##b=float(input("Ingrese otro valor:"))
##promedio=(a+b)/2
##print("Su promedio es:",promedio)

##Ejercicio 6 F
##Escribir un programa en la computadora que imprima en pantalla
##Mi primer programa Python

##print("Mi primer programa python")

##Ejercicio 7
##Escribir un programa en la computadora que imprima en pantalla
##v
##e
##r
##t
##i
##c
##a
##l


##print("v\ne\nr\nt\ni\nc\na\nl")


##Ejercicio 8 F
##Escribir un programa en Python que imprima la siguiente gura en la pantalla:
##  *****
##  *   *
##  *   *
##  *   *
##  *****
##con un solo print.

##print("*****\n*   *\n*   *\n*   *\n*****")


##Ejercicio 9 F
##Escribir un programa en Python que imprima la siguiente gura en la pantalla utilizando un solo
##print:
#*
#***
#*****
#*******
#*********

##print("*\n***\n****\n*****\n******\n*******")


##Ejercicio 11 F
##Escribir un programa en Python que pida al usuario que ingrese un valor y luego imprima en la
##pantalla:
##******************************
##* El resultado es: <valor>
##******************************
##donde en vez de <valor> debe mostrarse el valor que el usuario ingresó por teclado.



##valor=input("Ingrese un valor:")
##largoAsterisco=len(valor)+21
##print("*"*largoAsterisco)
##print("* El resultado es:",valor,"*")
##print("*"*largoAsterisco)


##Ejercicio 13 F
##Suponga que una persona desea invertir su capital en un banco y quiere saber cuánto dinero tendrá en
##su cuenta si el banco incrementa el 6 % mensual(no acumulativo). Se le debe pedir al usuario el capital
##a invertir y la cantidad de meses.

##inversion = float(input("Ingrese el monto a invertir"))
##meses = int(input("Ingrese la cantidad de meses"))
##incremento = float((6*inversion)/100)
##acumulado = float(incremento*meses)
##print("Inversion inicial: ", inversion)
##print("Cantidad de meses: ", meses)
##print("Incremento mensual: ", incremento)
##print("Incremento al final del plazo: ", acumulado+inversion)



##Ejercicio 14 F
##Una empresa telefónica desea un programa para calcular el importe de sus clientes. Sabiendo que el
##costo por comunicación es de $3 y por cada segundo se cobra $0, 25 hacer dicho programa. Se deben
##ingresar la cantidad de llamadas realizadas y el tiempo total de comunicación, el programa debe devolver
##el precio a cobrar.


##cantidad_Llamadas=int(input("Ingrese cantidad de llamadas:"))
##tiempo_Comunicacion=float(input("Ingrese el tiempo de comunicacion:"))
##precioAcobrar= (cantidad_Llamadas*3)+(tiempo_Comunicacion*0.25)
##print("El precio a cobrar es:",precioAcobrar)


##Ejercicio 15 F
##Un vendedor recibe un sueldo base de $7000 más un 10 % extra del total de sus ventas, el vendedor
##desea saber cuánto dinero obtendrá en total en el mes si ha logrado realizar 3 ventas este mes. Tenga en
##cuenta el sueldo básico y la comisión por las ventas. Hacer un programa que solicite el monto de cada
##una de las ventas del mes e indique cuál será el sueldo nal del vendedor.

##venta1=float(input("Ingrese el valor de venta:"))
##venta2=float(input("Ingrese el valor de venta:"))
##venta3=float(input("Ingrese el valor de venta:"))
##sueldoBase=7000
##sueldoFinal=(venta1+venta2+venta3)*10/100+sueldoBase
##print("El sueldo final es:",sueldoFinal)





##Ejercicio 19 F
##Escribir en Python un programa que pida al usuario que ingrese dos valores y los guarde en dos
##variables, x e y. El programa deberá intercambiar los valores de x e y y luego mostrar en pantalla:
##El valor de x es: <x>
##El valor de y es: <y>
##donde en lugar de <x> e <y> deberá mostrarse el valor de las respectivas variables


##x=int(input("Ingrese un valor:"))
##y=int(input("Ingrese un valor:"))
##aux=x
##x=y
##y=aux
##
##print("El valor de x es:",x)
##print("El valor de y es:",y)





##Ejercicio 20 F
##Escribir en Python un programa que pida al usuario que ingrese tres valores y los guarde en tres
##variables, x, y, y z. El programa deberá intercambiar circularmente los valores de x, y y z, es decir, x
##debe tomar el valor de y, y el de z y z el de x. Y luego mostrarlos en pantalla:
##El valor de x es: <x>
##El valor de y es: <y>
##El valor de z es: <z>
##donde en lugar de <x>, <y> y <z> deberá mostrarse el valor de las respectivas variables.



##x=int(input("Ingrese un valor:"))
##y=int(input("Ingrese un valor:"))
##z=int(input("Ingrese un valor:"))
##aux=x
##x=y
##y=z
##z=aux
##
##print("El valor de x es:",x)
##print("El valor de y es:",y)
##print("El valor de z es:",z)










