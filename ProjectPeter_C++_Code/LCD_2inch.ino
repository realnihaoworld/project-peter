#include <SPI.h>
#include "LCD_Driver.h"
#include "GUI_Paint.h"
#include "image.h"

void setup()
{
  Config_Init();
  LCD_Init();
  LCD_Clear(0xffff);
  Paint_NewImage(LCD_WIDTH, LCD_HEIGHT, 0, WHITE);
  Paint_Clear(WHITE);
  // Paint_DrawString_EN(30, 10, "123", &Font24, YELLOW, RED);
  // Paint_DrawString_EN(30, 34, "ABC", &Font24, BLUE, CYAN);
  
  // Paint_DrawString_CN(50,180, "微雪电子",  &Font24CN, WHITE, RED);
  
  // Paint_DrawRectangle(125, 10, 225, 58, RED,  DOT_PIXEL_2X2,DRAW_FILL_EMPTY);
  // Paint_DrawLine(125, 10, 225, 58, MAGENTA,   DOT_PIXEL_2X2,LINE_STYLE_SOLID);
  // Paint_DrawLine(225, 10, 125, 58, MAGENTA,   DOT_PIXEL_2X2,LINE_STYLE_SOLID);
  
  // Paint_DrawCircle(150,100, 25, BLUE,   DOT_PIXEL_2X2,   DRAW_FILL_EMPTY);
  // Paint_DrawCircle(180,100, 25, BLACK,  DOT_PIXEL_2X2,   DRAW_FILL_EMPTY);
  // Paint_DrawCircle(210,100, 25, RED,    DOT_PIXEL_2X2,   DRAW_FILL_EMPTY);
  // Paint_DrawCircle(165,125, 25, YELLOW, DOT_PIXEL_2X2,   DRAW_FILL_EMPTY);
  // Paint_DrawCircle(195,125, 25, GREEN,  DOT_PIXEL_2X2,   DRAW_FILL_EMPTY);
  
  

  //Paint_DrawImage(gImage_70X70, 20, 80, 70, 70); 
  //Paint_DrawFloatNum (5, 150 ,987.654321,4,  &Font20,    WHITE,   LIGHTGREEN);

}
void loop()
{
  fuck_u();
}
void eyes(){
  Paint_DrawRectangle(10, 10, 120, 160, BLUE,  DOT_PIXEL_2X2, DRAW_FILL_EMPTY);
  Paint_DrawRectangle(200, 10, 310, 160, BLUE,  DOT_PIXEL_2X2 , DRAW_FILL_EMPTY);
  Paint_DrawRectangle(50, 40, 80, 130, BLACK,  DOT_PIXEL_4X4, BLACK);
  Paint_DrawRectangle(240, 40, 270, 130, BLACK,  DOT_PIXEL_4X4, BLACK);
  Paint_DrawRectangle(10, 180, 250, 210, RED, DOT_PIXEL_4X4, BLACK);

}
void missing_phone(){
  Paint_DrawString_EN(85, 50, "WARNING", &Font24, BLUE, CYAN);
  Paint_DrawString_EN(30, 100, "PHONE NOT FOUND", &Font24, BLUE, CYAN);
}
void reset(){
  LCD_Clear(0xffff);
  Paint_NewImage(LCD_WIDTH, LCD_HEIGHT, 0, WHITE);
}
void fuck_u(){
  reset();
  Paint_DrawString_EN(90, 80, "FUCK YOU", &Font24, BLUE, CYAN);

}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
