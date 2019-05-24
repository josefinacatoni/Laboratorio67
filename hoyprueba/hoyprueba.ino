int dato;

void setup()
 
{
 
Serial.begin(9600);
 
}
 
void loop()
 
{
dato = analogRead(A1);
Serial.println(dato);
 
//delay(100);
exit(1);
}
