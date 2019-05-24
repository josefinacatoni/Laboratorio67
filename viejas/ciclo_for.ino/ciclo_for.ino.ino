/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/AnalogReadSerial

  Este programa hace un loop de 10 pasos que imprime en cada paso los datos medidos en el canal A1
*/
#define SIZE 50 //define una variable fija constante para todo el codigo
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() //loop infinito para tomar datos
{
  int i;
  int tiempo[SIZE];
  int voltaje[SIZE];
  // read the input on analog pin 0:
  for (i=0; i<SIZE; i ++)  //solo hasta 10 valores
  {
    
    tiempo[i]= millis();
    voltaje[i] = analogRead(A1);
    // print out the value you read:
    Serial.print(tiempo[i]);
    Serial.print("\t");
    Serial.println(voltaje[i]); //imprime los valores del canal A1
  
    delay(10);  // delay in between reads for stability
    //Serial.print(i);
  }

   /* FILE *fp;
  fp=fopen("resultados.txt","a");
  fprintf(fp,"Tiempo \t Voltaje \n");  // Encabezado del archivo
  for (int i = 0; i < SIZE; ++i){
    fprintf(fp,"%.5lg \t\t %.5lg \n",tiempo[i],voltaje[i]);
  }
  fclose(fp);*/
  
 exit(0); //para terminar el loop (Un unico loop)
}
  
