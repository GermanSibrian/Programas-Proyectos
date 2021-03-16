########################3 NÚMEROS########################
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
        archivo=open('Promedio.txt','a');
        try:
            if (opcion==1):
                print ('####################################');
                x = int(input('     INGRESE EL PRIMER NÚMERO: '));
                print ('####################################');
                y = int(input('     INGRESE EL SEGUNDO NÚMERO: '));
                print ('####################################');
                z = int(input('     INGRESE EL TERCER NÚMERO: '));
                prom=((x+y+z)/3);
                if (prom >=60):
                    print ('####################################');
                    print ('      EL PROMEDIO ES: ', prom      );
                    print ('####################################');
                    print ('#             APROBADO             #');
                    print ('####################################');
                    dato=str(prom);
                    archivo.write('\n');
                    archivo.write('EL PROMEDIO ES DE: '+dato+'\n');
                    archivo.write('APROBADO\n')
                    archivo.close()
                    opcion = int(input("              OPCIÓN: "));
                elif (prom <60):
                    print ('####################################');
                    print ('      EL PROMEDIO ES: ', prom      );
                    print ('####################################');
                    print ('#             REPROBADO            #');
                    print ('####################################');
                    dato=str(prom);
                    archivo.write('\n');
                    archivo.write('EL PROMEDIO ES DE: '+dato+'\n');
                    archivo.write('REPROBADO\n')
                    archivo.close()
                    opcion = int(input("              OPCIÓN: "));
            elif (opcion==2):
                print ('####################################');
                print ('#              HISTORIAL           #');
                print ('####################################');
                archivo=open('Promedio.txt','r')
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