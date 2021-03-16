########################AÑO########################
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

opcion = int(input("              OPCIÓN: "));

while (opcion<=2):
        archivo=open('Año.txt','a');
        if(opcion==1):
            try:
                print ('####################################');
                x=int(input('        INGRESE UN AÑO: '));
                dato=str(x);
                if(x % 4 ==0):
                    print ('####################################');
                    print ('#        ES UN AÑO BISIESTO        #');
                    print ('####################################');
                    archivo.write('\n');
                    archivo.write('EL AÑO ' +dato+ ' ES UN AÑO BISIESTO\n');
                    archivo.close()
                    opcion = int(input("              OPCIÓN: "));
                elif(x % 4 != 0):
                    print ('####################################');
                    print ('#       NO ES UN AÑO BISIESTO      #');
                    print ('####################################');
                    archivo.write('\n');
                    archivo.write('EL AÑO ' +dato+ ' NO ES UN AÑO BISIESTO\n');
                    archivo.close()
                    opcion = int(input("              OPCIÓN: "));
            except(ValueError):
                print ('####################################');
                print ('#       HA OCURRIDO UN ERROR       #');
                print ('####################################');
        elif (opcion==2):
            print ('####################################');
            print ('#              HISTORIAL           #');
            print ('####################################');
            archivo=open('Año.txt','r')
            historial=archivo.read()
            archivo.close();
            print(historial)
            opcion = int(input("              OPCIÓN: "));

