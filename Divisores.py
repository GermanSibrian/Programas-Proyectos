########################DIVISORES########################
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
        archivo=open('Divisores.txt','a')
        try:
            print ('####################################');
            numero = int(input('     ENCONTRAR DIVISORES DE: '));
            print ('####################################');
            contador = 0;
            if numero==0 or numero<0:
                print ('#    ELIJA UN NÚMERO MAYOR QUE 0   #');
            elif numero>0:
                print ('#        LOS DIVISORES SON         #');
                print ('####################################');
                for divisor in range(1, numero+1):
                    if (numero % divisor)==0:
                        print(divisor)
                        contador +=1
                print ('####################################');
                num=str(numero);
                cont=str(contador);
                div=str([divisor  for divisor in range(1, numero+1) if numero % divisor==0]);
                archivo.write('\n');
                archivo.write('LOS DIVISORES DE '+num+' SON: '+div+'\n')
                archivo.write(num+ ' TIENE '+cont+' DIVISORES \n')
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
