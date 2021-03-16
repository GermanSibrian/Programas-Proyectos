########################TRIÁNGULOS########################
print ('####################################');
print ('#         ELIJA UNA OPCIÓN         #');
print ('####################################');
print ('************************************');
print ('#       1. INICIAR/CONTINUAR       #');
print ('************************************');
print ('#           2. HISTORIAL           #');
print ('************************************');
print ('#             3. SALIR             #');
print ('************************************');
try:
    opcion = int(input("              OPCIÓN: "));
    while (opcion<=2):
        try:
            if (opcion==1):
                print ('####################################');
                x = float(input('     INGRESE EL PRIMER NÚMERO: '));
                print ('####################################');
                y = float(input('     INGRESE EL SEGUNDO NÚMERO: '));
                print ('####################################');
                z = float(input('     INGRESE EL TERCER NÚMERO: '));
                archivo=open('Triángulo.txt','a');
                a=str(x);
                b=str(y);
                c=str(z);
                if (x>0 and y>0 and z>0 and x==y and x==z):
                    print ('####################################');
                    print ('     EL TRIÁNGULO ES: EQUILÁTERO'    );
                    print ('####################################');
                    archivo.write('\n');
                    archivo.write('LOS LADOS DEL TRIÁNGULO SON:'' x= '+a+', y= '+b+', z= '+c+ '\n' )
                    archivo.write('EL TRIÁNGULO ES EQUILÁTERO\n');
                    archivo.close();
                    opcion = int(input("              OPCIÓN: "));
                elif (x>0 and y>0 and z>0 and x==z and y!=x):
                    print ('####################################');
                    print ('      EL TRIÁNGULO ES: ISÓCELES'     );
                    print ('####################################');
                    archivo.write('\n');
                    archivo.write('LOS LADOS DEL TRIÁNGULO SON:'' x= '+a+', y= '+b+', z= '+c+ '\n' )
                    archivo.write('EL TRIÁNGULO ES ISÓCELES\n');
                    archivo.close();
                    opcion = int(input("              OPCIÓN: "));
                elif (x>0 and y>0 and z>0 and x==y and z!=y):
                    print ('####################################');
                    print ('      EL TRIÁNGULO ES: ISÓCELES'     );
                    print ('####################################');
                    archivo.write('\n');
                    archivo.write('LOS LADOS DEL TRIÁNGULO SON:'' x= '+a+', y= '+b+', z= '+c+ '\n' )
                    archivo.write('EL TRIÁNGULO ES ISÓCELES\n');
                    archivo.close();
                    opcion = int(input("              OPCIÓN: "));
                elif (x>0 and y>0 and z>0 and y==z and x!=z):
                    print ('####################################');
                    print ('      EL TRIÁNGULO ES: ISÓCELES'     );
                    print ('####################################');
                    archivo.write('\n');
                    archivo.write('LOS LADOS DEL TRIÁNGULO SON:'' x= '+a+', y= '+b+', z= '+c+ '\n' )
                    archivo.write('EL TRIÁNGULO ES ISÓCELES\n');
                    archivo.close();
                    opcion = int(input("              OPCIÓN: "));
                elif (x>0 and y>0 and z>0 and y!=x and y!=z and x!=z):
                        #if (y>z):
                    print ('####################################');
                    print ('      EL TRIÁNGULO ES: ESCALENO'     );
                    print ('####################################');
                    archivo.write('\n');
                    archivo.write('LOS LADOS DEL TRIÁNGULO SON:'' x= '+a+', y= '+b+', z= '+c+ '\n' )
                    archivo.write('EL TRIÁNGULO ES ESCALENO\n');
                    archivo.close();
                    opcion = int(input("              OPCIÓN: "));
                elif (x<0 or y<0 or z<0 ):
                    print ('####################################');
                    print ('  ERROR: INGRESE NÚMEROS POSITIVOS  ');
                    print ('####################################');
                    opcion = int(input("              OPCIÓN: "));
            elif opcion==2:
                print ('####################################');
                print ('#              HISTORIAL           #');
                print ('####################################');
                archivo=open('Triángulo.txt','r')
                historial=archivo.read()
                archivo.close();
                print(historial)
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