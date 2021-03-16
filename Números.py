########################3 NÚMEROS########################
print ('####################################');
print ('#         ELIJA UNA OPCIÓN         #');
print ('####################################');
print ('************************************');
print ('#       1. INICIAR/CONTINUAR       #');
print ('************************************');
print ('#             2. SALIR             #');
print ('************************************');
try:
    opcion = int(input("              OPCIÓN: "));
    while (opcion<=1):
        try:
            print ('####################################');
            x = float(input('     INGRESE EL PRIMER NÚMERO: '));
            print ('####################################');
            y = float(input('     INGRESE EL SEGUNDO NÚMERO: '));
            print ('####################################');
            z = float(input('     INGRESE EL TERCER NÚMERO: '));
            archivo=open('Números.txt','a')
            a=str(x)
            b=str(y)
            c=str(z)
            if (opcion==1):
                if (x>y and x>z):
                        #if (x>z):
                    print ('####################################');
                    print ('      EL RESULTADO ES: ', x+y+z      );
                    print ('####################################');
                    resul=str(x+y+z)
                    archivo.write('\n');
                    archivo.write('LOS NÚMEROS INGRESADOS SON: '+a+', '+b+', '+c+'\n');
                    archivo.write('EL RESULTADO ES: '+resul+'\n');
                    archivo.close();
                    opcion = int(input("              OPCIÓN: "));
                elif (x==z and y!=x):
                    print ('####################################');
                    print ('      EL NÚMERO DIFERENTE ES: ', y   );
                    print ('####################################');
                    resul=str(y)
                    archivo.write('\n');
                    archivo.write('LOS NÚMEROS INGRESADOS SON: '+a+', '+b+', '+c+'\n');
                    archivo.write('EL NÚMERO DIFERENTE ES: '+resul+'\n');
                    archivo.close();
                    opcion = int(input("              OPCIÓN: "));
                elif (x==y and z!=y):
                    print ('####################################');
                    print ('      EL NÚMERO DIFERENTE ES: ', z   );
                    print ('####################################');
                    resul=str(z)
                    archivo.write('\n');
                    archivo.write('LOS NÚMEROS INGRESADOS SON: '+a+', '+b+', '+c+'\n');
                    archivo.write('EL NÚMERO DIFERENTE ES: '+resul+'\n');
                    archivo.close();
                    opcion = int(input("              OPCIÓN: "));
                elif (y==z and x!=z):
                    print ('####################################');
                    print ('      EL NÚMERO DIFERENTE ES: ', x   );
                    print ('####################################');
                    resul=str(x)
                    archivo.write('\n');
                    archivo.write('LOS NÚMEROS INGRESADOS SON: '+a+', '+b+', '+c+'\n');
                    archivo.write('EL NÚMERO DIFERENTE ES: '+resul+'\n');
                    archivo.close();
                    opcion = int(input("              OPCIÓN: "));
                elif (y>x and y>z):
                        #if (y>z):
                    print ('####################################');
                    print ('      EL RESULTADO ES: ', x*y*z      );
                    print ('####################################');
                    resul=str(x*y*z)
                    archivo.write('\n');
                    archivo.write('LOS NÚMEROS INGRESADOS SON: '+a+', '+b+', '+c+'\n');
                    archivo.write('EL RESULTADO ES: '+resul+'\n');
                    archivo.close();
                    opcion = int(input("              OPCIÓN: "));
                elif (z>x and z>y):
                        #if (z>y):
                    print ('####################################');
                    print ('   EL RESULTADO ES: '+str(a)+', '+str(b)+', '+str(c)   );
                    print ('####################################');
                    archivo.write('\n');
                    archivo.write('LOS NÚMEROS INGRESADOS SON: '+a+', '+b+', '+c+'\n');
                    archivo.write('EL RESULTADO ES: '+str(a)+', '+str(b)+', '+str(c)+ '\n');
                    archivo.close();
                    opcion = int(input("              OPCIÓN: "));
                elif (y==x==z):
                        #if (y>z):
                    print ('####################################');
                    print ('#   LOS TRES NÚMEROS SON IGUALES   #');
                    print ('####################################');
                    archivo.write('\n');
                    archivo.write('LOS NÚMEROS INGRESADOS SON: '+a+', '+b+', '+c+'\n');
                    archivo.write('LOS NÚMEROS SON IGUALES\n');
                    archivo.close();
                    opcion = int(input("              OPCIÓN: "));
        except(ValueError):
            print ('####################################');
            print ('#       HA OCURRIDO UN ERROR       #');
            print ('#       VUELVA A INTENTARLO        #');
            print ('####################################');
            opcion = int(input("              OPCIÓN: "));
except(ValueError):
    print ('####################################');
    print ('#       HA OCURRIDO UN ERROR       #');
    print ('####################################');