#include <stdint.h>

int main(void)
{
	//Registros del GPIOB a partir de la direccion: 0x40020400
	// 0x40020400 + 0x00 = 0x40020400 //Direccion registro RegModer (Offset de 0x00 porque es el primer registro del GPIOB)
	// 0x40020400 + 0x14 = 0x40020414 //Direccion registro Odr del GPIOB (Offset de 0x14)
	// 0x40023800 + 0x30 = 0x40023830 //Direccion registro RCC_AHB1ENR
	uint32_t *p_RegModerGPIOB = (uint32_t *) 0x40020400;
	uint32_t *p_OdrGPIOB = (uint32_t *) 0x40020414;
	
	//Cuando se quiera usar un GPIO se debe activar el clock de ese GPIO
	//Esto se encuentra en el registro RCC_AHB1ENR que pertenece a RCC, con offset de direccion 0x30
	uint32_t * p_ClockEnableGPIOB = (uint32_t *) 0x40023830;
	
	*p_ClockEnableGPIOB |= 0x00000002; //Activa el GPIOB. Hce un OR con el registro y el dato (0x00000002)
	*p_RegModerGPIOB &= 0xFFFFFFF0; //Primero se limpia el registro para el GPIOB
	*p_RegModerGPIOB |= 0x00000001; //Convierte en GPIO
	*p_OdrGPIOB |= 0x00000001; //Enciende el GPIOB

	for(;;);
}
