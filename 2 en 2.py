########################2 EN 2########################
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
    archivo=open('2 En 2.txt', 'a')
    if (opcion==1):
        print ('####################################');
        x = int(input('     INGRESE EL PRIMER NÚMERO: '));
        print ('####################################');
        y = int(input('     INGRESE EL SEGUNDO NÚMERO: '));
        print ('####################################');
        dato1=str(x)
        dato2=str(y)
        if (x<=y):
            for n in range(x,y+1,2):
                num = str(n)
                print(n)
            mayor=str([n  for n in range(x,y+1,2) if x<=y]);
            archivo.write('\n');
            archivo.write('EL NÚMERO MAYOR ES '+dato2+ ' Y SE ORDENAN '+mayor+ '\n');
            archivo.close()
            opcion = int(input("              OPCIÓN: "));
        elif (x >= y):
            for n in range(x, y - 1, -2):
                num = str(n)
                print(n)
            mayor=str([n  for n in range(x,y-1,-2) if x>=y]);
            archivo.write('\n');
            archivo.write('EL NÚMERO MAYOR ES '+dato1+ ' Y SE ORDENAN '+mayor+ '\n');
            archivo.close()
            opcion = int(input("              OPCIÓN: "));

30