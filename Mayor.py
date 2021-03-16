
########################MAYOR A MENOR########################
print ('####################################');
print ('#         ELIJA UNA OPCIÓN         #');
print ('####################################');
print ('************************************');
print ('#       1. INICIAR/CONTINUAR       #');
print ('************************************');
print ('#             2. SALIR             #');
print ('************************************');
opcion = int(input("              OPCIÓN: "));
while (opcion<=1):
            print ('####################################');
            x = int(input('     INGRESE EL PRIMER NÚMERO: '));
            print ('####################################');
            y = int(input('     INGRESE EL SEGUNDO NÚMERO: '));
            print ('####################################');
            dato1=str(x)
            dato2=str(y)
            archivo=open('Mayor a menor.txt', 'a')
            archivo.write('\n');
            if (opcion==1):
                if (x>y):
                    print ('####################################');
                    print ('    EL MAYOR ES EL PRIMER NÚMERO    ');
                    print ('####################################');
                    print("       EL NÚMERO MAYOR ES:",x)
                    for n in range(x,y-1,-1):
                        print(n)
                    mayor=str([n  for n in range(x,y-1,-1) if x>y]);
                    opcion = int(input("              OPCIÓN: "));
                    archivo.write('EL NÚMERO MAYOR ES '+dato1+ ' Y SE ORDENAN '+mayor+ '\n');
                    archivo.close()

                elif (y>x):
                    print ('####################################');
                    print ('    EL MAYOR ES EL SEGUNDO NÚMERO   ');
                    print ('####################################');
                    print("       EL NÚMERO MAYOR ES:",y)
                    for n in range(y,x-1,-1):
                        print(n)
                    mayor=str([n  for n in range(y,x-1,-1) if y>x]);
                    archivo.write('EL NÚMERO MAYOR ES '+dato2+ ' Y SE ORDENAN '+mayor+ '\n');
                    archivo.close()
                    opcion = int(input("              OPCIÓN: "));
                else:
                    print ('####################################');
                    print ('     LOS DOS NÚMEROS SON IGUALES    ');
                    print ('####################################');
                    archivo.write('LOS DOS NÚMEROS SON IGUALES \n');
                    archivo.close()
                    opcion = int(input("              OPCIÓN: "));