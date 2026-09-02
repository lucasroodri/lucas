#include <stdio.h>
#include <stdint.h> //Libreria estandar para el manejo de enteros

int main()
{
	printf("Clase 2 \r\n");

	uint16_t variable1 = 32133; //Crea una variable unsigned entera de 16 bits
	int16_t variable2;
	int32_t _variable; //Las variables pueden empezar por "_"

	printf("Valor variable: %d \r\n", variable1);

	//float: variable de 32 bits para decimales de maximo 7 decimales
	float var_f = 3.1415926;
	printf("Pi es igual a: %f \r\n", var_f); //El identificador de float es %f
	printf("Pi es igual a: %0.2f \r\n", var_f); //Se puede especificar el numero de decimales que aparecen
	float var_f_e = 112.34567e3;
	printf("%f en notacion cientifica es igual a: %e \r\n", var_f_e,var_f_e); //Con %e te dice el valor en notacion cientifica

	float var_f_dec = 1.1234567891011;
	printf("Mi valor es: %f \r\n", var_f_dec); //De esta manera solo enseña 6 decimales
	printf("Mi valor es: %0.13f \r\n", var_f_dec); //Tampoco asi muestra bien el valor

	//double: variable de 64 bits para decimales de maximo 15 decimales
	double var_d = 1.1234567891011;
	printf("Mi variable es: %lf \r\n", var_d); //Se usa el identificador %lf para el double
	printf("Mi variable es: %0.13lf \r\n", var_d); //Para que muestre todos los decimales hay que especificarlo
	printf("Mi variable en not. cient. es: %0.13le \r\n", var_d); //La notacion cientifica del double es con %le

	double var_electron = -1.60217662e-19;
	printf("El valor del electron es: %0.15lf \r\n", var_electron); //Sale todo cero porque es muy pequeño
	printf("El valor del electron es: %0.28lf \r\n", var_electron);
	printf("El valor del electron en not. cient. es: %0.15le \r\n", var_electron);

	//Operadoes Matematicos
	uint16_t x = 5;
	uint16_t y = 10;
	uint16_t res_sum, res_rest, res_mult, res_div;
	uint16_t res_oper;

	res_sum = x + y;
	res_rest = y - x;
	res_mult = x * y;
	res_div = y / x;
	res_oper = x + y * 2;

	printf("Resultado de la suma: %d \n", res_sum);
	printf("Resultado de la resta: %d \n", res_rest);
	printf("Resultado de la multiplicacion: %d \n", res_mult);
	printf("Resultado de la division: %d \n", res_div);
	printf("Resultado de la operacion: %d \r\n", res_oper);

    return 0;
}