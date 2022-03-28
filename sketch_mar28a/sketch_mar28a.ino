#include <Servo.h>     //libreria para el servomotor

Servo servo;  // crea el objeto servo

void setup() {
  Serial.begin(9600);
  servo.attach(8);  // vincula el servo al pin digital 9
 
 }

void loop() {

 if(Serial.available()>0)
   {     
      char data= Serial.read(); // leer "data" del modulo bluetooth
      switch(data) //abrir casos correspondientes a los datos introducidos en "data"
      {
        case '1': servo.write(0);delay(500);;
        case '3': servo.write(90);delay(500);break;
        case '2': servo.write(180);delay(500);break;
        default : break;
      }
      Serial.println(data);
   }
   delay(50);
}
