########################IMPARES########################
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


            archivo=open('Impares.txt','a')
            if opcion==1:
                print ('####################################');
                numero = int(input('      ENCONTRAR IMPARES DE:  '));
                print ('####################################');
                if numero==0 or numero<0:
                    print ('#    ELIJA UN NÚMERO MAYOR QUE 0   #');
                elif numero>0:
                    print ('#         LOS IMPARES SON          #');
                    print ('####################################');
                    print( [n  for n in range(1, numero+1) if n % 2])
                    print ('####################################');
                    contador = int((numero+1)/2)
                    impares=str(contador);
                    num=str([n  for n in range(1, numero+1) if n % 2]);
                    dato=str(numero);
                    print ('   EL NÚMERO DE IMPARES ES DE:', contador);
                    print ('####################################');
                    archivo.write("\n");
                    archivo.write('LOS IMPARES DE '+dato+ ' SON:'+num+'\n' );
                    archivo.write(dato+ ' TIENE: ' +impares+ ' NÚMEROS IMPARES\n' );
                    archivo.close();
                    opcion = int(input("              OPCIÓN: "));

            elif opcion==2:
                print ('####################################');
                print ('#              HISTORIAL           #');
                print ('####################################');
                archivo=open('Impares.txt','r')
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
