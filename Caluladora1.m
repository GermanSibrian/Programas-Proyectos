clear all
Inicio= 0;
while Inicio == 0
    disp ('******************************************');
    disp ('*************ELIJA UNA OPCIÓN*************');
    disp ('******************************************');
    disp ('');
    disp ('******************************************');
    disp ('Suma = 1');
    disp ('******************************************');
    disp ('Resta = 2');
    disp ('******************************************');
    disp ('Multiplicación = 3');
    disp ('******************************************');
    disp ('División = 4');
    disp ('******************************************');
    disp ('Salir = 5');
    disp ('******************************************');
    opcion = input ('OPERACIÓN ');
    switch opcion
        case 1, disp('******************SUMA********************');
            x = input ('Ingrese el primer número ');
            y = input ('Ingrese el segundo número ');
            z = x+y;
            fprintf('El resultado es = %d\n', z)
            salida = input ('¿Desea continuar? (si/no) ','s');
            if salida == 's'
                Inicio = 0;
                clc
            elseif salida == 'n'
                Inicio = 1;
            end
        case 2, disp('******************RESTA*******************');
            x = input ('Ingrese el primer número ');
            y = input ('Ingrese el segundo número ');
            z = x-y;
            fprintf('El resultado es = %d\n', z)
            salida = input ('¿Desea continuar? (si/no) ','s');
            if salida == 's'
                Inicio = 0;
                clc
            elseif salida == 'n'
                Inicio = 1;
            end
        case 3, disp('*************MULTIPLICACIÓN***************');
            x = input ('Ingrese el primer número ');
            y = input ('Ingrese el segundo número ');
            z = x*y;
            fprintf('El resultado es = %d\n', z)
            salida = input ('¿Desea continuar? (si/no) ','s');
            if salida == 's'
                Inicio = 0;
                clc
            elseif salida == 'n'
                Inicio = 1;
            end
        case 4, disp('****************DIVISIÓN******************');
            x = input ('Ingrese el primer número ');
            y = input ('Ingrese el segundo número ');
            z = x/y;
             if y == 0
                disp ('Operación no permitida');
                Inicio=1;
            else 
            fprintf('El resultado es = %d\n', z)
            salida = input ('¿Desea continuar? (si/no) ','s');
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