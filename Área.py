import math
########################ÁREAS########################
print ('####################################');
print ('#         ELIJA UNA OPCIÓN         #');
print ('####################################');
print ('************************************');
print ('#            1. CÍRCULO            #');
print ('************************************');
print ('#           2. TRIÁNGULO           #');
print ('************************************');
print ('#            3. CUADRADO           #');
print ('************************************');
print ('#          4. RECTÁNGULO           #');
print ('************************************');
print ('#          5. HISTORIAL            #');
print ('************************************');
print ('#             6. SALIR             #');
print ('************************************');
try:
    opcion = int(input("              OPCIÓN: "));
    while (opcion<=5):
        try:
            archivo=open('Área.txt','a')
            if (opcion==1):
                print ('####################################');
                x = float(input('        INGRESE EL RADIO: '));
                print ('####################################');
                print ('   EL ÁREA DEL CÍRCULO ES: ', math.pi*pow(x,2));
                print ('####################################');
                area=str(math.pi*pow(x,2))
                radio=str(x);
                archivo.write('\n');
                archivo.write('ÁREA DE UN CÍRCULO DE RADIO: '+radio+ '\n');
                archivo.write('EL ÁREA DEL CÍRCULO ES: '+area+'\n')
                opcion = int(input("              OPCIÓN: "));
            elif (opcion==2):
                print ('####################################');
                y = float(input('        INGRESE LA BASE: '));
                z = float(input('        INGRESE LA ALTURA: '));
                print ('####################################');
                print ('   EL ÁREA DEL TRIÁNGULO ES: ', 0.5*z*y);
                print ('####################################');
                area=str(0.5*z*y)
                base=str(z);
                altura=str(y);
                archivo.write('\n');
                archivo.write('ÁREA DE UN TRIÁNGULO DE BASE: '+base+ ' Y ALTURA: '+altura+ '\n');
                archivo.write('EL ÁREA DEL TRIÁNGULO ES: '+area+'\n')
                opcion = int(input("              OPCIÓN: "));
            elif (opcion==3):
                print ('####################################');
                w = float(input(' INGRESE LA LONGITUD DE LADO: '));
                print ('####################################');
                print ('   EL ÁREA DEL CUADRADO ES: ', pow(w,2));
                print ('####################################');
                opcion = int(input("              OPCIÓN: "));
                area=str(pow(w,2))
                lado=str(w);
                archivo.write('\n');
                archivo.write('ÁREA DE UN CUADRADO DE LADO: '+lado+'\n');
                archivo.write('EL ÁREA DEL CUADRADO ES: '+area+'\n')
                opcion = int(input("              OPCIÓN: "));
            elif (opcion==4):
                print ('####################################');
                p = float(input(' INGRESE LA LONGITUD DE UN LADO: '));
                q = float(input(' INGRESE LA LONGITUD DE OTRO LADO: '));
                print ('####################################');
                print ('   EL ÁREA DEL RECTANGULO ES: ', p*q);
                print ('####################################');
                area=str(p*q)
                lado1=str(p);
                lado2=str(q);
                archivo.write('\n');
                archivo.write('ÁREA DE UN RECTANGULO DE LADOS: '+lado1+ ' Y : '+lado2+ '\n');
                archivo.write('EL ÁREA DEL RECTANGULOO ES: '+area+'\n')
                opcion = int(input("              OPCIÓN: "));
            elif (opcion==5):
                print ('####################################');
                print ('#              HISTORIAL           #');
                print ('####################################');
                archivo=open('Área.txt','r')
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