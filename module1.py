########################FACTORIAL########################
print ('******************************************');
print ('*************ELIJA UNA OPCIÓN*************');
print ('******************************************');
print ('******************************************');
print ('Calcular factorial = 1');
print ('******************************************');
print ('Salir = 2');
print ('******************************************');
opcion = int(input("OPERACIÓN\n"))
def factorial(n):
   if n==0 or n==1:
            resultado=1
   elif n>1:
            resultado=n*factorial(n-1)
   elif n<0:
            resultado="No existente"
   return resultado
try:
    while (opcion<=1):
            print ('******************************************');
            fact= int(input("NÚMERO\n"))
            fac=factorial(fact)
            print ('******************************************');
            archivo = open("factorial.txt", "a");
            dato = str(fact)
            resul = str(fac)
            if (opcion==1):
                print ('******************************************');
                print('El factorial es: ',fac)
                print ('******************************************');
                archivo.write("El factorial de " + dato + " es: " + resul);
                archivo.write("\n");
                archivo.close()
                opcion = int(input("OPERACIÓN\n"))
except(ValueError):
            archivo = open("factorial.txt", "a");
            archivo.write("No se puede determinar el factorial");
            archivo.write("\n");
            archivo.close()
            print ('Ha ocurrido un error')