########################REPETICIÓN########################
print ('####################################');
print ('#         ELIJA UNA OPCIÓN         #');
print ('####################################');
print ('************************************');
print ('#       1. INICIAR/CONTINUAR       #');
print ('************************************');
print ('#             2. SALIR             #');
print ('************************************');
opcion = int(input("              OPCIÓN: "));
print ('************************************');
def pedir_palabra():
    num = 0
    num = str(input("              PALABRA: "))
    return num
while (opcion<=1):
    archivo=open('Repetición.txt','a')
    palabra= pedir_palabra()
    letras=palabra.lower()
    print ('************************************');
    if (opcion==1):
        a=letras.count("a")
        e=letras.count("e")
        i=letras.count("i")
        o=letras.count("o")
        u=letras.count("u")
        x=str(a);
        y=str(e);
        z=str(i);
        p=str(o);
        q=str(u);
        print("La palabra",palabra,"tiene:")
        print("A=",a)
        print("E=",e)
        print("I=",i)
        print("O=",o)
        print("U=",u)
        print ('************************************');
        opcion = int(input("              OPCIÓN: "));
        print ('************************************');
        archivo.write('\n');
        archivo.write('LA PALABRA '+palabra+ ' TIENE:\n');
        archivo.write(x+'\n');
        archivo.write(y+'\n');
        archivo.write(z+'\n');
        archivo.write(p+'\n');
        archivo.write(q+'\n');
        archivo.close();

