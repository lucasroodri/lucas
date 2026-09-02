/*
 * main.c
 *
 *  Created on: 1 sept 2026
 *      Author: lucas
 */

#include <stdio.h>

int main()
{
    printf("Hola Mundo\n");
    printf("\tHey\n"); //Hay varias opciones con la barra invertida

    printf("123456789\r"); //El retorno de carro vuelve al principio de la linea y ejecuta la siguiente instruccion
    printf("Hola\n");        //En este caso sobrescribe 123456789 con Hola

    //ESPECIFICADORES DE FORMATO
    printf("Clase Numero %d + %d = %d \r\n",5,2,5+2); //Se sustituye %d por lo que haya en cada coma
    //Existen mas especificadores de formato

    //VARIABLES
    //char: 1 byte de codigo que almacena un caracter ASCII
    char var_char = '1';
    printf("Mi primer caracter: %c \r\n",var_char);

    //sizeof: devuelve el tamaño en bytes de una variable
    printf("El tamaño de la variable var_char: %c es de: %d Byte \r\n",var_char,sizeof(var_char));

    signed char var_signed = -15; //Signed va desde -128 a 127
    unsigned char var_unsigned = 200; //Unsigned va desde 0 hasta 255
    printf("Numero con signo: %d que tiene un tamaño de %d Byte \r\n",var_signed,sizeof(var_signed));
    printf("Numero sin signo: %d que tiene un tamaño de %d Byte \r\n",var_unsigned,sizeof(var_unsigned));

    //int: Dato entero que puede ocupar 2 o 4 bytes de memoria, depende del hardware
    //STM32 --> 32 Bits: 4 Bytes
    //PIC18 --> 8 Bits: 2 Bytes
    unsigned int var_u_int = 123232;
    signed int var_s_int = -575096;
	printf("Numero con signo: %d que tiene un tamaño de %d Bytes \r\n",var_s_int,sizeof(var_s_int));
    printf("Numero sin signo: %d que tiene un tamaño de %d Bytes \r\n",var_u_int,sizeof(var_u_int));

    //short: Se usa para crear variables int de 2 bytes
    unsigned short var_u_short = 12632;
    signed short var_s_short = -12096;
    printf("Numero con signo: %d que tiene un tamaño de %d Bytes \r\n",var_s_short,sizeof(var_s_short));
    printf("Numero sin signo: %d que tiene un tamaño de %d Bytes \r\n",var_u_short,sizeof(var_u_short));

    //long: Se usa para crear variables de 4 o 8 bytes (Depende del hardware)
    //4 bytes
    unsigned long var_u_long = 123832;
    signed long var_s_long = -57796;
	printf("Numero con signo: %lld que tiene un tamaño de %d Bytes \r\n",var_s_long,sizeof(var_s_long));
    printf("Numero sin signo: %lld que tiene un tamaño de %d Bytes \r\n",var_u_long,sizeof(var_u_long));

    //8 Bytes
    unsigned long long var_u_long_long = 1233423452;
    signed long long var_s_long_long = -575432446;
    printf("Numero con signo: %ld que tiene un tamaño de %d Bytes \r\n",var_s_long_long ,sizeof(var_s_long_long ));
    printf("Numero sin signo: %ld que tiene un tamaño de %d Bytes \r\n",var_u_long_long ,sizeof(var_u_long_long ));

    return 0;
}

