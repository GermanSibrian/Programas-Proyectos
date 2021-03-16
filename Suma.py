########################SUMA########################
print ('####################################');
print ('#         ELIJA UNA OPCIÓN         #');
print ('####################################');
print ('************************************');
print ('#       1. INICIAR/CONTINUAR       #');
print ('************************************');
print ('#             2. SALIR             #');
print ('************************************');
opcion = int(input("           OPERACIÓN:"))
def factorial(n):
   if n==1:
            resultado=1
   elif n>1:
            resultado=n+factorial(n-1)
   elif n==0:
            resultado=0
   return resultado
try:
    while (opcion<=1):
            suma=0;
            print ('####################################');
            fact= int(input("           NÚMERO: "))
            fac=factorial(fact)
            print ('####################################');
            archivo = open("Suma.txt", "a");
            dato = str(fact)
            resul = str(fac)
            if (opcion==1):
                    temp = []
                    for num in range(1,fact+1):
                        temp.append(str(num))
                        suma=suma+num
                    f = " + ".join(temp)
                    dat=str(f)
                    print(f," = ",suma)
            print ('####################################');
            print('          LA SUMA ES: ',fac)
            archivo.write("\n");
            print ('####################################');
            archivo.write("LOS COEFICIENTES DE " + dato +" SON: " +dat+"\n");
            archivo.write("LA SUMA DE LOS COEFICIENTES DE " + dato + " ES: " + resul+"\n");
            archivo.close()
            opcion = int(input("           OPERACIÓN:"))
except(ValueError):
    archivo = open("factorial.txt", "a");
    archivo.write("NO SE PUEDE DETERMINAR LA SUMA");
    archivo.write("\n");
    archivo.close()
    print ('####################################');
    print ('#       HA OCURRIDO UN ERROR       #');
    print ('####################################');
