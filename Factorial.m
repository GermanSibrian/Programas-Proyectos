clc
clear all
close all
Inicio= 0;
while Inicio == 0
    disp ('******************************************');
    disp ('*************ELIJA UNA OPCIÓN*************');
    disp ('******************************************');
    disp ('');
    disp ('******************************************');
    disp ('Factorial = 1');
    disp ('******************************************');
    disp ('Salir = 2');
    disp ('******************************************');
    opcion = input ('OPERACIÓN ');
try  
        switch opcion
        case 1, disp('******************Factorial********************');
            x=input('Ingrese un número: ');
            fac=1;
            for n=1:x
                fac=fac*n;
            end
            if x < 0 
              fac = 'No definido';
            end
            disp('El factorial es: ');
            disp (fac);
            archivo = fopen('Factorial.txt','at');
            fprintf(archivo,'El factorial de %g, es %g \n', x, fac);
            fclose(archivo);
            salida = input ('¿Desea continuar? (si/no) ','s');
            if salida == 's'
                Inicio = 0;
                clc
            elseif salida == 'n'
                Inicio = 1;
            end
        case 2, disp('*****************SALIR********************');
            Inicio = 1;
        end
 catch
        disp('*****************SALIR********************')
        Inicio = 1;
 end
 end 
