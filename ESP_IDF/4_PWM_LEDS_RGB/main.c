#include <stdio.h>
#include "driver/gpio.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_log.h" //Libreria para Logs
#include "freertos/timers.h" //Libreria de Timers
#include "driver/ledc.h" //Libreria que permite el uso de PWM 

#define led1 2 //Se define el LED2 (GPIO2) que es el pin4
static const char* tag = "Main";
uint8_t led_level = 0;
TimerHandle_t xTimers;
int interval = 50;
int timerId = 1;
int dutyR = 0;
int dutyG = 300;
int dutyB = 700;

esp_err_t init_led(void); //Se declaran funciones. En este casos para inicializar el led
esp_err_t blink_led(void); //En este caso para el parpadeo del led

esp_err_t set_timer(void); //Funcion de inicializacion del timer

esp_err_t set_pwm(void);
esp_err_t set_pwm_duty(void);

void vTimerCallback(TimerHandle_t pxTimer){ //Callback del Timer
  dutyR += 10;
  if(dutyR > 1023){
    dutyR = 0;
  }
  dutyG += 10;
  if(dutyG > 1023){
    dutyG = 0;
  }
  dutyB += 10;
  if(dutyB > 1023){
    dutyB = 0;
  }

  blink_led();
  set_pwm_duty();
}

void app_main(){ 
  init_led();
  set_pwm();
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

esp_err_t set_pwm(void){
  ledc_channel_config_t channelConfigR = {0}; //Se crea un array vacio
  channelConfigR.gpio_num = 33;
  channelConfigR.speed_mode = LEDC_HIGH_SPEED_MODE; 
  channelConfigR.channel = LEDC_CHANNEL_0; //Para cada salida PWM se usa un canal diferente
  channelConfigR.intr_type = LEDC_INTR_DISABLE; //No se habilita una interrupcion
  channelConfigR.timer_sel = LEDC_TIMER_0;
  channelConfigR.duty = 0;

  ledc_channel_config_t channelConfigG = {0}; //Se crea un array vacio
  channelConfigG.gpio_num = 25;
  channelConfigG.speed_mode = LEDC_HIGH_SPEED_MODE; 
  channelConfigG.channel = LEDC_CHANNEL_1; //Para cada salida PWM se usa un canal diferente
  channelConfigG.intr_type = LEDC_INTR_DISABLE; //No se habilita una interrupcion
  channelConfigG.timer_sel = LEDC_TIMER_0;
  channelConfigG.duty = 0;

  ledc_channel_config_t channelConfigB = {0}; //Se crea un array vacio
  channelConfigB.gpio_num = 26;
  channelConfigB.speed_mode = LEDC_HIGH_SPEED_MODE; 
  channelConfigB.channel = LEDC_CHANNEL_2; //Para cada salida PWM se usa un canal diferente
  channelConfigB.intr_type = LEDC_INTR_DISABLE; //No se habilita una interrupcion
  channelConfigB.timer_sel = LEDC_TIMER_0;
  channelConfigB.duty = 0;

  ledc_channel_config(&channelConfigR); //La configuracion se manda como puntero
  ledc_channel_config(&channelConfigG);
  ledc_channel_config(&channelConfigB);

  ledc_timer_config_t timerConfig = {0}; //Configurador del Timer global
  timerConfig.speed_mode = LEDC_HIGH_SPEED_MODE;
  timerConfig.duty_resolution = LEDC_TIMER_10_BIT;
  timerConfig.timer_num = LEDC_TIMER_0;
  timerConfig.freq_hz = 20000;

  ledc_timer_config(&timerConfig);


  return ESP_OK;
}

esp_err_t set_pwm_duty(void){
  ledc_set_duty(LEDC_HIGH_SPEED_MODE, LEDC_CHANNEL_0, dutyR); //Establece el duty del PWM
  ledc_set_duty(LEDC_HIGH_SPEED_MODE, LEDC_CHANNEL_1, dutyG);
  ledc_set_duty(LEDC_HIGH_SPEED_MODE, LEDC_CHANNEL_2, dutyB);

  ledc_update_duty(LEDC_HIGH_SPEED_MODE, LEDC_CHANNEL_0); //Actualiza el duty del PWM correctamente 
  ledc_update_duty(LEDC_HIGH_SPEED_MODE, LEDC_CHANNEL_1);
  ledc_update_duty(LEDC_HIGH_SPEED_MODE, LEDC_CHANNEL_2);


  return ESP_OK;
}