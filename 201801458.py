import psycopg2 as p
########################3 NÚMEROS########################
#Constantes Globales:
PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "1234"
PSQL_DB   = "germansibrian"
#########################################################
########################3 NÚMEROS########################
print ('####################################');
print ('#         ELIJA UNA OPCIÓN         #');
print ('####################################');
print ('************************************');
print ('#           1. PROGRAMA  1         #');
print ('************************************');
print ('#           2. PROGRAMA  2         #');
print ('************************************');
print ('#           3. PROGRAMA  3         #');
print ('************************************');
print ('#           4. PROGRAMA  4         #');
print ('************************************');
print ('#           5. PROGRAMA  5         #');
print ('************************************');
print ('#             6. SALIR             #');
print ('************************************');
opcion = int(input("           OPERACIÓN:"))
connection =p.connect(host=PSQL_HOST, database=PSQL_DB, user=PSQL_USER, password=PSQL_PASS)
cursor = connection.cursor()

def fibonacci(d):
	a=0
	b=1
	for k in range(d):
		c=a+b
		a=b
		b=c
	return b

def adicion(n):
	if n==1:
	    resultado=1
	elif n>1:
	    resultado=n+adicion(n-1)
	elif n==0:
	    resultado=0
	return resultado
while (opcion<=3):
	archivo = open("201801458.txt", "a");
	if (opcion==1):
		suma=0;
		suma2=0;
		print ('####################################');
		fact= int(input("           NÚMERO: "))
		fac=adicion(fact)
		print ('####################################');
		temp = []
		for num in range(1,fact+1):
		    temp.append(str(num))
		    suma=suma+(num*num)
		    suma2=suma2+num
		    suma3=suma2*suma2
		    res=suma3-suma
		    f = " + ".join(temp)
		    dat=str(f)
		                    #print(suma)
		                    #print('\n')
		                    #print(suma2)
		                    #print('\n')
		                    #print(suma3)
		                    #print('\n')
		                    #print(res)
		dato=str(suma);
		dato2=str(suma3);
		resu=str(res);
		print ('   EL RESULTADO DE RESTAR: '+str(suma3)+' - '+str(suma)+' ES '+str(res));
		archivo.write("\n");
		print ('####################################');
		archivo.write("LA RESTA DE " +dato2+" - " +dato+ " ES " +resu+"\n");
		archivo.close()
		opcion = int(input("           OPERACIÓN:"))
		SQL = "INSERT INTO programa1(numero, suma_cuadrados, cuadrado_suma, respuesta) VALUES ('%s','%s','%s','%s');"
		datos = (num, suma, suma3, res);
		cursor.execute(SQL,datos)
		connection.commit()

	if (opcion==2):

		y = int(input('     INGRESE UN NÚMERO: '));
		y1=str(y)
		print('\n')
		print('LA SERIE DE FIBONACCI ES: \n')
		for e in range(y):
			print(fibonacci(e))
		opcion = int(input("           OPERACIÓN:"))
		archivo.write('\n');
		archivo.write('LA SERIE DE FIBONACCI DE '+y1+ ' ES '+str(fibonacci(e))+ '\n');
		archivo.close()

	if (opcion==3):
		y = int(input('     INGRESE UN NÚMERO: '));
		pri = []
		div = []
		for i in range (1,y+1):
			if y%i == 0:
				div.append(i)
			else:
				i = i
		def prim(numero):
			for n in range(2, numero):
				if numero % n == 0:
					return False
			pri.append(numero)
			return True
		for i in range(0, len(div)):
			prim(div[i])
		z = len(pri) - 1
		mayor = pri[z]
		archivo.write('\n');
		archivo.write('EL PRIMO MÁS GRANDE DE ' +str(y)+ ' ES '+str(mayor)+ '\n');
		archivo.close()
		print ('####################################');
		print("EL PRIMO MÁS GRANDE ", mayor)
		print ('####################################');
		opcion = int(input("           OPERACIÓN:"))
		SQL = "INSERT INTO programa2(numero, primo) VALUES ('%s','%s');"
		datos = (y, mayor);
		cursor.execute(SQL,datos)
		connection.commit()
cursor.close()
connection.close()