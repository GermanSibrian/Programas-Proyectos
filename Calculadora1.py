########################CALCULADORA########################
print ('******************************************');
print ('*************ELIJA UNA OPCIÓN*************');
print ('******************************************');
print ('******************************************');
print ('Suma = 1');
print ('******************************************');
print ('Resta = 2');
print ('******************************************');
print ('Multiplicación = 3');
print ('******************************************');
print ('División = 4');
print ('******************************************');
print ('Salir = 5');
print ('******************************************');
opcion = int(input("OPERACIÓN\n"))
try:
    while (opcion<=4):

        print ('******************************************');
        x = float(input('Ingrese un número\n'))
        print ('******************************************');
        y = float(input('Ingrese otro número\n'))
        print ('******************************************');
        if (opcion==1):
            print ('******************************************');
            print('El resultado es: ',x+y)
            print ('******************************************');
            opcion = int(input("OPERACIÓN\n"))
        elif (opcion==2):
            print ('******************************************');
            print('El resultado es: ',x-y)
            print ('******************************************');
            opcion = int(input("OPERACIÓN\n"))
        elif (opcion==3):
            print ('******************************************');
            print('El resultado es: ',x*y)
            print ('******************************************');
            opcion = int(input("OPERACIÓN\n"))
        elif (opcion==4):
            try:
                print ('******************************************');
                print('El resultado es: ',x/y)
                print ('******************************************');
                opcion = int(input("OPERACIÓN\n"))
            except ZeroDivisionError:
                print ('******************************************');
                print('La división entre 0 no es permitida')
                print ('******************************************');
                opcion = int(input("OPERACIÓN\n"))
except(ValueError):
            print ('Ha ocurrido un error, vuelva a intentarlo');