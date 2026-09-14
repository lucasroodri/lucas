#include <stdio.h>
#include "driver/gpio.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_log.h" //Libreria para Logs
#include "freertos/timers.h" //Libreria de Timers

#define led1 2 //Se define el LED2 (GPIO2) que es el pin4
static const char* tag = "Main";
uint8_t led_level = 0;
TimerHandle_t xTimers;
int interval = 500;
int timerId = 1;

esp_err_t init_led(void); //Se declaran funciones. En este casos para inicializar el led
esp_err_t blink_led(void); //En este caso para el parpadeo del led

esp_err_t set_timer(void); //Funcion de inicializacion del timer

void vTimerCallback(TimerHandle_t pxTimer){ //Callback del Timer
  ESP_LOGI(tag, "Event was called from Timer");
  blink_led();
}

void app_main(){ 
  init_led();
  set_timer();
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

esp_err_t set_timer(void){
  ESP_LOGI(tag, "Timer init configuration");
  //Todo esto se puede copiar de los ejemplos disponibles en la Libreria
  xTimers = xTimerCreate( //Se crea el Timer. Tiene 5 parametros
    "Timer", //Se le pone un nombre al Timer
    (pdMS_TO_TICKS(interval)), //El perido del Timer en ticks (periodo de la CPU). pdMS_TO_TICKS convierte la variable intervall(= 100) en ms
    pdTRUE, //Con pdTRUE se indica que cuando se acabe el Timer se autoreinicie
    (void *)timerId, //Asigna al Timer un ID
    vTimerCallback //Se especifica el Callback que llamara el Timer cuando se agote
  );

  if(xTimers == NULL){
    //El timer no esta creado
    ESP_LOGE(tag, "Timer was not created");
  }else{
    //Comienza el Timer
    if(xTimerStart(xTimers, 0) != pdPASS){
      //El timer no se pudo activar
      ESP_LOGE(tag, "Timer could not be set to Active state");
    }
  }

  return ESP_OK;
}