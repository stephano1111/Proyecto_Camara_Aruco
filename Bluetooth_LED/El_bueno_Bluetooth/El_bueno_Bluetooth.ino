
#include <SoftwareSerial.h>


void setup(){
  
 pinMode(13, OUTPUT);
 pinMode(11, OUTPUT);
 // initialize the serial communications:
 Serial.begin(9600);
 digitalWrite(13,LOW);//activar bluetooth
 delay(1000);
 digitalWrite(13,HIGH);
}

void loop(){
  
 if(Serial.available()>0){ //Comprobamos si en el buffer hay datos
   char dato;
   dato = Serial.read();  //Lee cada carácter uno por uno y se almacena en una variable
   Serial.println(dato);  //Imprimimos en la consola el carácter recibido
   
   if (dato == 'o'){
      digitalWrite(11,HIGH);
   }
   else {
      digitalWrite(11, LOW);
   }
   
 }

}
