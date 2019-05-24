int analogPin = A0; //  connected to analog pin 0
int tiempo;                 
int val = 0;  // variable to store the value read
int i=0;

int tiempos = {};
int volt;

void setup() {
  Serial.begin(1000000);           //  setup serial
}


void loop() {
  // turn off tone function for pin 7:
  noTone(6);
  // play a note on pin 8 for 300 ms:
  tone(6, 65, 10000);
  delay(100);
  
  while (i<100)
  {
    //tiempos =+ millis();
    //volt =+ analogRead(analogPin);  // read the input pin
    //Serial.print(tiempos);
    //Serial.print("\t");
    //Serial.print(volt);          // debug value
    //Serial.print("\t");
    tiempo=millis();
    val=analogRead(analogPin);
    tiempos+=tiempo;
    volt+=val;
    //tiempos.concat(tiempo);
    //tiempos.concat("\t");
    //volt.concat(val);
    //volt.concat("\t"); // read the input pin
    
    //Serial.println(i);
     Serial.println(tiempos);
    //Serial.print("\t"); 
    Serial.println(volt);
    delay(100);
    i++;
  }
  
Serial.println(tiempos);
//Serial.print("\t");
Serial.println(volt);

exit(1);

}
