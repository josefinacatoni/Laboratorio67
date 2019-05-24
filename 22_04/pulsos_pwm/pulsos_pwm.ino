// Este programa genera pulsos con frecuencia f0 desde el pin6 y lee la respuesta conectada a la entrada analogica A0


int pwm_pin = 6; 
int mes_pin = A0;
int output;
int pwm_value;

void setup() 
{
    pinMode(pwm_pin, OUTPUT);

}

void loop() 
{
  output = analogRead(mes_pin);
  //Mapping the Values between 0 to 255 because we can give output
  //from 0 -255 using the analogwrite funtion
  pwm_value = map(output, 0, 1023, 0, 255);
  //analogWrite(pwm_pin, pwm_value);

  Serial.println(output);
  delay(10);

//exit(0);
}
