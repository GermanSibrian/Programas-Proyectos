clear all
Inicio= 0;
while Inicio == 0
    disp ('******************************************');
    disp ('*************ELIJA UNA OPCI�N*************');
    disp ('******************************************');
    disp ('');
    disp ('******************************************');
    disp ('Suma = 1');
    disp ('******************************************');
    disp ('Resta = 2');
    disp ('******************************************');
    disp ('Multiplicaci�n = 3');
    disp ('******************************************');
    disp ('Divisi�n = 4');
    disp ('******************************************');
    disp ('Salir = 5');
    disp ('******************************************');
    opcion = input ('OPERACI�N ');
    switch opcion
        case 1, disp('******************SUMA********************');
            x = input ('Ingrese el primer n�mero ');
            y = input ('Ingrese el segundo n�mero ');
            z = x+y;
            fprintf('El resultado es = %d\n', z)
            salida = input ('�Desea continuar? (si/no) ','s');
            if salida == 's'
                Inicio = 0;
                clc
            elseif salida == 'n'
                Inicio = 1;
            end
        case 2, disp('******************RESTA*******************');
            x = input ('Ingrese el primer n�mero ');
            y = input ('Ingrese el segundo n�mero ');
            z = x-y;
            fprintf('El resultado es = %d\n', z)
            salida = input ('�Desea continuar? (si/no) ','s');
            if salida == 's'
                Inicio = 0;
                clc
            elseif salida == 'n'
                Inicio = 1;
            end
        case 3, disp('*************MULTIPLICACI�N***************');
            x = input ('Ingrese el primer n�mero ');
            y = input ('Ingrese el segundo n�mero ');
            z = x*y;
            fprintf('El resultado es = %d\n', z)
            salida = input ('�Desea continuar? (si/no) ','s');
            if salida == 's'
                Inicio = 0;
                clc
            elseif salida == 'n'
                Inicio = 1;
            end
        case 4, disp('****************DIVISI�N******************');
            x = input ('Ingrese el primer n�mero ');
            y = input ('Ingrese el segundo n�mero ');
            z = x/y;
             if y == 0
                disp ('Operaci�n no permitida');
                Inicio=1;
            else 
            fprintf('El resultado es = %d\n', z)
            salida = input ('�Desea continuar? (si/no) ','s');
                if salida == 's'
                    Inicio = 0;
                    clc
                elseif salida == 'n'
                    Inicio = 1;
                end
             end
            case 5, disp('*****************SALIR********************');
            Inicio = 1;
    end
end 