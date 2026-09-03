#include <stdio.h>
#include <stdint.h> //Libreria estandar para el manejo de enteros

int main()
{
	printf("Clase 3 \r\n");

	int data = 17;
	char variable = '0'; //ASCII: 48 decimal
	int suma_t = data + variable;
	printf("Suma: %d \r\n", suma_t); //Se puede sumar un int con un char porque suma el valor decimal del char

	uint32_t var1_int = 22;
	uint32_t var2_int = 5;
	float resul_div_float = var1_int / var2_int;
	printf("Resultado de division: %.3f \r\n", resul_div_float); //Da 4.000 en vez de 4.400 porque al dividir enteros el 
                                                                 //resultado siempre es entero

	float var1_f = 22;
	float var2_f = 5;
	float res_f = var1_f / var2_f;
	printf("Resultado de division: %.3f \r\n", res_f);  //Ahora si es un float

	//Cast: Convertir una variable de un tipo en otro. Puede ser implicito o explicito
	//Cast implicito: Por ejemplo cuando el compilador convierte un char en su valor decimal
	//Cast explicito: El programador especifica la conversion que se va a realizar
	uint32_t var1 = 22, var2 = 5;
	float res_cast = (float) var1 / var2;
	printf("Resultado de division tras Cast: %.3f \r\n", res_cast);

	//Mas operadores matematicos
	//Modulo: Devuelve el resto de una division. Solo se puede usar con enteros
	uint32_t var_mod1 = 51, var_mod2 = 5;
	uint32_t res_mod = var_mod1 % var_mod2;
	printf("Resto de la division: %d \r\n", res_mod);

	float var_modf1 = 51.0, var_modf2 = 5.0;
	//uint32_t res_modf = var_modf1 % var_modf2; //Da error por hacer el modulo a un float
	//printf("Resto de la division: %d \r\n", res_modf); //Da error

	//Incremento
	uint32_t var_incr1 = 5, var_incr2 = 5;
	uint32_t tot_incr1 = (++var_incr1) + 5; //Primero hace el incremento y luego el resto de operacion
	uint32_t tot_incr2 = (var_incr2++) + 5; //Hace la operacion y luego incrementa la variable
	printf("Resultado 1: %d \r\n", tot_incr1);
	printf("Resultado 2: %d \r\n", tot_incr2);
	printf("Valor var_incr2: %d \r\n", var_incr2);

	//Decremento: Es analogo a Incremento y se usa --

	//Punteros: Pueden ser Address y Pointer
	//Address: Cada variable se almacena en la memoria. Para saber su direccion se usa & delante de la variable
	//Pointer: Contiene la direccion de una variable o funcion. Con el operador "*" se indica que es un puntero a
	uint32_t temp = 15;
	printf("Valor de temp: %d \r\n", temp);
	uint32_t *p; //Se crea un puntero a un entero
	p = &temp; //Se mete en el puntero la direccion de var_x
	printf("La direccion de memoria de temp es: %p \r\n", p); //Para ver la direcc. del puntero se usa %p

	*p = 25; //Esto mete en la direccion del puntero el valor 25. Es decir en la variable temp
	printf("Valor de temp: %d \r\n", temp);
	//Lectura de punteros
	uint32_t valor_p = *p; //Se puede usar con otras variables
	printf("Valor de valor_p: %d \r\n", valor_p);

	//Los punteros se deben de crear del miso tipo de la variable a la que va a apuntar. Si no son iguales se
	//puede hacer antes un cast
	uint32_t otro_temp = 500;
	printf("Valor de otro_temp: %d \r\n", otro_temp);
	char *otro_p = (char *)&otro_temp; //Al ser un puntero en el cast hay que poner tambien *
	printf("Direccion de memoria de otro_temp: %p \r\n", otro_p);
	*otro_p = 2;
	printf("Valor de otro_temp: %d \r\n", otro_temp); //No guarda bien el valor porque el puntero es a char y es de 8 bits
													  //Hay que tener en cuenta cuando se haga un cast de puntero que tipo se va a usar 

	
    return 0;
}