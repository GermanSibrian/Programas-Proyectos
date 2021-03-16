########################FACTORIAL 7########################
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
    while(opcion<=2):
        if (opcion==1):
            def pedir_numero():
                correcto = False
                num = 0
                while (not correcto):
                    try:
                        print ('####################################');
                        num = int(input("              NÚMERO: "))
                        if (num>0):
                            correcto = True
                        else:
                            print ('####################################');
                            print ('#    INGRESE UN ENTERO POSITIVO    #')
                            print ('####################################');
                    except ValueError:
                        print ('####################################');
                        print ('#       HA OCURRIDO UN ERROR       #');
                        print ('#       VUELVA A INTENTARLO        #');
                        print ('####################################');
                return num
            salir = False
            archivo=open('Factorial 7.txt','a');
            opcion = 0
            fac = pedir_numero()
            factorial=1
            if (fac % 7 ==0):
                for n in range(fac):
                    factorial = factorial * (n + 1)
                dato=str(fac);
                resul=str(factorial);
                print ('####################################');
                print("    EL FACTORIAL ES: ", factorial);
                print ('####################################');
                archivo.write('\n');
                archivo.write('EL FACTORIAL DE '+dato+ ' ES: '+resul+'\n');
                archivo.close();
                opcion = int(input("              OPCIÓN: "));
            else:
                print ('####################################');
                print ('#     INGRESE UN MÚLTIPLO DE 7     #')
                print ('####################################');
                opcion = int(input("              OPCIÓN: "));
        elif opcion==2:
                print ('####################################');
                print ('#              HISTORIAL           #');
                print ('####################################');
                archivo=open('Factorial 7.txt','r')
                historial=archivo.read()
                archivo.close();
                print(historial)
                opcion = int(input("              OPCIÓN: "));
except(ValueError):
    print ('####################################');
    print ('#       HA OCURRIDO UN ERROR       #');
    print ('####################################');