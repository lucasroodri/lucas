#include <stdio.h>
#include "driver/gpio.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#define led1 2 //Se define el LED2 (GPIO2) que es el pin4

uint8_t led_level = 0;

esp_err_t init_led(void); //Se declaran funciones. En este casos para inicializar el led
esp_err_t blink_led(void); //En este caso para el parpadeo del led


void app_main() {
  init_led();

  while(1){
    vTaskDelay(500 / portTICK_PERIOD_MS); //Se usa el delay de la libreria task. Se divide entre eso para que sean 200 ms
    blink_led();
    printf("Led level: %d\n", led_level);
  }
}

esp_err_t init_led(void){
  gpio_reset_pin(led1); //Se reseta el pin
  gpio_set_direction(led1, GPIO_MODE_OUTPUT); //Se convierte al GPIO en una salida
  return ESP_OK; //Se usa en ESP IDF para verificar que ha ido bien
}

esp_err_t blink_led(void){
  led_level = !led_level;
  gpio_set_level(led1, led_level);
  return ESP_OK;
}