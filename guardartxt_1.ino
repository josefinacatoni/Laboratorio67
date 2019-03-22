int recordData[20]; // Array will store key input presses with 1 equal pressed and 0 equal not pressed
char serInString[10]; 
void setup() {
   //pinMode(ledPin, OUTPUT); 
   Serial.begin(9600);
   Serial.println("ready");
  // println(Serial.list()); 
  delay(1000);
}
int x=0;
unsigned long time;
void loop() 
{
// read the input on analog pin 0:
  //for (x=0; x<50; x ++)  //solo hasta 10 valores
  //{
    int sensorValue = analogRead(A1);
    time=millis();
    // print out the value you read:
    
  
    //
    Serial.print(time);
    Serial.print("\t");
    Serial.println(sensorValue); //imprime los valores del canal A1
  
    delay(100);  // delay in between reads for stability
    //Serial.println(x);
  //}
 exit(0); //para terminar el loop (Un unico loop)
}
