########################AUTOMÓVILES########################
def pedir_numero_menú():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("OPCIÓN: "))
            print()
            correcto = True
        except ValueError:
            print ('####################################');
            print ('#       HA OCURRIDO UN ERROR       #');
            print ('#       VUELVA A INTENTARLO        #');
            print ('####################################');
    return num

def pedir_numero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("INFORMACIÓN: "))
            if (num>0):
                correcto = True
            else:
                print ('####################################');
                print ('#       HA OCURRIDO UN ERROR       #');
                print ('#       VUELVA A INTENTARLO        #');
                print ('####################################');
        except ValueError:
            print ('####################################');
            print ('#       HA OCURRIDO UN ERROR       #');
            print ('#       VUELVA A INTENTARLO        #');
            print ('####################################');
    return num

salir = False
opcion = 0
while (not salir):
    print ('####################################');
    print ('#         ELIJA UNA OPCIÓN         #');
    print ('####################################');
    print ('************************************');
    print ('#       1. INICIAR/CONTINUAR       #');
    print ('************************************');
    print ('#            2. HISTORIAL          #');
    print ('************************************');
    print ('#              3. SALIR            #');
    print ('************************************');
    opcion = pedir_numero_menú()
    if opcion==1:
        archivo = open("Taxi.txt", "a")
        print ('####################################');
        print("#               MODELO              #")
        modelo = pedir_numero()
        modelo1=str(modelo)
        print ('####################################');
        print("#            KILOMETRAJE            #")
        kilometraje = pedir_numero()
        kilometraje1=str(kilometraje)
        archivo.write("INFORMACIÓN DEL VEHÍCULO")
        archivo.write("\n")
        archivo.write("EL VEHÍCULO ES MODELO: "+modelo1)
        archivo.write("\n")
        archivo.write("TIENE "+ kilometraje1+" KILOMETROS RECORRIDOS.")
        archivo.write("\n")
        if (modelo<2007) and (kilometraje>20000):
            print("NECESITA RENOVARSE\n")
            archivo.write("NECESITA RENOVARSE")
            archivo.write("\n")
            archivo.write("\n")
        elif (modelo>=2007) and (modelo<=2013) and (kilometraje<=20000) and (kilometraje>=10000):
            print("NECESITA MANTENIMIENTO\n")
            archivo.write("NECESITA MANTENIMIENTO")
            archivo.write("\n")
            archivo.write("\n")
        elif (modelo>2013) and (modelo<=2021) and (kilometraje<10000):
            print("ÓPTIMAS CONDICIONES\n")
            archivo.write("ÓPTIMAS CONDICIONES")
            archivo.write("\n")
            archivo.write("\n")
        else:
            print("MECÁNICO")
            archivo.write("MECÁNICO\n")
            archivo.write("\n")
            archivo.write("\n")
    elif opcion == 2:
        archivo = open("Taxi.txt", "r")
        historial = archivo.read()
        archivo.close()
        print(historial)
    elif opcion==3:
        salir = True

    else:
        print("INGRESE UN NÚMERO DEL MENÚ\n")
