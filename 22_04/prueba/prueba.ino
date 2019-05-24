//int analogPin0 = A0; //  connected to analog pin 0
int analogPin1 = A1; //  connected to analog pin 1
//int analogPin2 = A2; //  connected to analog pin 2
//int analogPin3 = A3; //  connected to analog pin 3
//int analogPin4 = A4; //  connected to analog pin 4
int tiempo;  
int val0 = 0;  // variable to store the value read               
int val1 = 0;  // variable to store the value read
int val2 = 0;  // variable to store the value read
int val3 = 0;  // variable to store the value read
int val4 = 0;  // variable to store the value read
int i=0;

String tiempos = {};
String volt;

void setup() {
  Serial.begin(57600);           //  setup serial
}


void loop() {
  // turn off tone function for pin 7:
  noTone(2);
  noTone(6);
  // play a note on pin 2 of ... Hz:
  tone(6, 50000);
  delay(1000);
  
  while (i<10000)
  {
    tiempo= millis();
    Serial.print(tiempo);
    Serial.print("\t");
    //val0= analogRead(analogPin0);  // read the input pin
    
    val1= analogRead(analogPin1);  // read the input pin
    //val2= analogRead(analogPin2);  // read the input pin
    //val3= analogRead(analogPin3);  // read the input pin
    //val4= analogRead(analogPin4);  // read the input pin
      
    //Serial.println(val0);          // debug value
    
    //Serial.print("\t");
    Serial.println(val1);          // debug value
    //Serial.print("\t");
    //Serial.print(val2);          // debug value
    //Serial.print("\t");
    //Serial.print(val3);          // debug value
    //Serial.print("\t");
    //Serial.println(val4);          // debug value
    //Serial.println(i);

    //tiempos.concat(millis());
    //tiempos.concat("\t");
    //volt.concat(analogRead(analogPin));
    //volt.concat("\t"); // read the input pin
    
    //Serial.println(i);
     
    //delay(10);
    i++;
  }
  
//Serial.println(tiempos);
//Serial.print("\t");
//Serial.println(volt);

exit(1);

}
