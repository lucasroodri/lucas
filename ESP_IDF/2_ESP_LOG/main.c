#include <stdio.h>
#include "driver/gpio.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_log.h" //Libreria para Logs

#define led1 2 //Se define el LED2 (GPIO2) que es el pin4

static const char* tag = "Main";

uint8_t led_level = 0;
uint8_t count = 0;

esp_err_t init_led(void); //Se declaran funciones. En este casos para inicializar el led
esp_err_t blink_led(void); //En este caso para el parpadeo del led


void app_main() {
  init_led();

  while(1){
    vTaskDelay(200 / portTICK_PERIOD_MS); //Se usa el delay de la libreria task. Se divide entre eso para que sean 200 ms
    blink_led();

    count += 1;

    //EJEMPLO DE USOS DE LOG
    if(count > 30){
      count = 0;
    }
    if(count < 10){
      ESP_LOGI(tag, "Value: %u.", count); //Macro para mensaje de log. Este es de informacion (Verde)
    }
    if(count >= 10 && count < 20){
      ESP_LOGW(tag, "Value: %u.", count); //Warning (Amarillo)
    }
    if(count >= 20 && count < 30){
      ESP_LOGE(tag, "Value: %u.", count); //Error (Rojo)
    }
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