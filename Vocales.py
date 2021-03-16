########################VOCALES########################
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
    global txt;


    while opcion<=1:
        archivo=open('Vocales.txt','a')
        print ('####################################');
        txt=(input('    INGRESE UNA FRASE: '));
        tx=str(txt);
        print ('####################################');
        vocal=[
        "a","e","i","o","u","A","E","I","O","U",
        "á","é","í","ó","ú","Á","É","Í","Ó","Ú",
        "ä","ë","ï","ö","ü","Ä","Ë","Ï","Ö","Ü"]
        cont=0;
        for i in vocal:
            for j in txt:
                if(i==j):
                    cont=cont+1;
        n=str(cont);
        print("    EL NÚMERO DE VOCALES ES: ",cont);
        print ('####################################');
        archivo.write('\n');
        archivo.write('LA PALABRA '+tx+' TIENE '+n+' VOCALES\n');
        archivo.close()
        opcion = int(input("              OPCIÓN: "));
except(ValueError):
    print ('####################################');
    print ('#       HA OCURRIDO UN ERROR       #');
    print ('#       VUELVA A INTENTARLO        #');
    print ('####################################');