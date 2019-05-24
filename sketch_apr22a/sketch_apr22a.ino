
#include<avr/io.h>
#include <avr/iomxx0_1.h>
#include<util/delay.h>
void pwm_init()
{
        // Configure PB.7 as output pin
        DDRB |= (1<<PB7);
        TCCR1A =  (1<<WGM11) | (1<<WGM10) | (1<<COM1A1);
        TCCR1B =(1<<WGM12) | (1<<WGM13) | (1<<CS11);
        ICR1 = 51;
}

void pwm_generate()
{
    OCR1A = (50 * 52)/100 ;
}
int main()
{
pwm_init();
pwm_generate();
}
