#include <SPI.h>
#include "LCD_Driver.h"
#include "GUI_Paint.h"

int RED_MOOD = 2;
int BLUE_MOOD = 4;
int GREEN_MOOD = 3;
int PHONE_SENSOR = 5;
int BUZZER = 6;

void setup()
{
  pinMode(PHONE_SENSOR, INPUT);
  pinMode(RED_MOOD, OUTPUT);
  pinMode(BLUE_MOOD, OUTPUT);
  pinMode(GREEN_MOOD, OUTPUT);
  pinMode(BUZZER, OUTPUT);

  Config_Init();
  LCD_Init();
  LCD_Clear(0xffff);
  Paint_NewImage(LCD_WIDTH, LCD_HEIGHT, 0, WHITE);
  Paint_Clear(WHITE);
}
void loop()
{
  if(digitalRead(PHONE_SENSOR) == HIGH)
  {
    phone_located();
  }
  else if(digitalRead(PHONE_SENSOR) == LOW)
  {
    phone_missing();
  }
}
void phone_located(){
  reset();
  happy_led();
  Paint_DrawString_EN(85, 50, "CONGRATS", &Font24, BLUE, CYAN);                        //TEXT TO WARN FOR MISSING PHONE
  Paint_DrawString_EN(30, 100, "PHONE LOCATED", &Font24, BLUE, CYAN);

  if(digitalRead(PHONE_SENSOR) == LOW)
  {
    return;
  }

  delay(2000);

  if(digitalRead(PHONE_SENSOR) == LOW)
  {
    return;
  }

  reset();
  Paint_DrawRectangle(70, 30, 100, 150, BLACK,  DOT_PIXEL_2X2, BLACK);
  Paint_DrawRectangle(220, 30, 250, 150, BLACK,  DOT_PIXEL_2X2, BLACK);
  Paint_DrawLine(50, 130, 70, 150, BLACK,   DOT_PIXEL_2X2,LINE_STYLE_SOLID);
  Paint_DrawLine(270, 130, 290, 150, BLACK,   DOT_PIXEL_2X2,LINE_STYLE_SOLID);
  Paint_DrawLine(65, 150, 90, 170, BLACK,   DOT_PIXEL_2X2,LINE_STYLE_SOLID);
  Paint_DrawLine(250, 130, 275, 150, BLACK,   DOT_PIXEL_2X2,LINE_STYLE_SOLID);

  if(digitalRead(PHONE_SENSOR) == LOW)
  {
    return;
  }

  delay(2000);
}
void phone_missing(){
  reset();
  mad_led();
  Paint_DrawString_EN(85, 50, "WARNING", &Font24, BLUE, CYAN);                        //TEXT TO WARN FOR MISSING PHONE
  Paint_DrawString_EN(30, 100, "PHONE NOT FOUND", &Font24, BLUE, CYAN);
  
  if(digitalRead(PHONE_SENSOR) == HIGH)
  {
    return;
  }

  delay(2000);

  if(digitalRead(PHONE_SENSOR) == HIGH)
  {
    return;
  }

  reset();
  Paint_DrawRectangle(10, 10, 120, 160, RED,  DOT_PIXEL_2X2, DRAW_FILL_EMPTY);       //FACE FOR MISSING PHONE
  Paint_DrawRectangle(200, 10, 310, 160, RED,  DOT_PIXEL_2X2 , DRAW_FILL_EMPTY);
  Paint_DrawRectangle(50, 40, 80, 130, BLACK,  DOT_PIXEL_2X2, BLACK);
  Paint_DrawRectangle(240, 40, 270, 130, BLACK,  DOT_PIXEL_2X2, BLACK);
  Paint_DrawRectangle(150, 90, 170, 150, BLACK,  DOT_PIXEL_2X2, YELLOW);
  Paint_DrawRectangle(30, 180, 300, 210, RED, DOT_PIXEL_2X2, BLACK);

  if(digitalRead(PHONE_SENSOR) == HIGH)
  {
    return;
  }

  delay(2000);
}
void reset(){
  LCD_Clear(0xffff);
  Paint_NewImage(LCD_WIDTH, LCD_HEIGHT, 0, WHITE);
}
void happy_led(){
digitalWrite(BLUE_MOOD, HIGH);
digitalWrite(RED_MOOD, LOW);
analogWrite(BUZZER, LOW);
}
void mad_led(){
digitalWrite(BLUE_MOOD, LOW);
digitalWrite(RED_MOOD, HIGH);
for(int i=0; i<255; i++){
analogWrite(BUZZER, i);
}
}
void phone_check()
{
  if(digitalRead(PHONE_SENSOR) == HIGH)
  {
    return;
  }
}
