/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/AnalogReadSerial

  Este programa hace un loop de 10 pasos que imprime en cada paso los datos medidos en el canal A1
*/

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}


int x=0;

// the loop routine runs over and over again forever:
void loop() //loop infinito para tomar datos
{
  // read the input on analog pin 0:
  for (x=0; x<10; x ++)  //solo hasta 10 valores
  {
    int sensorValue = analogRead(A1);
    // print out the value you read:
    
  
    //
    Serial.println(sensorValue); //imprime los valores del canal A1
  
    delay(100);  // delay in between reads for stability
    //Serial.print(x);
  }
 exit(0); //para terminar el loop (Un unico loop)
}
  
