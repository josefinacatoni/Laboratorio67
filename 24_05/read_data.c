#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <fcntl.h>
#include <termios.h>
#include <errno.h>
#include <sys/ioctl.h>
#include <time.h>

#define MYPORT "/dev/ttyUSB0"
#define DELAY  3500000
#define DEBUG 1
#define NUM 60
 
// SPECIAL THANKS TO "www.chrisheydrick.com"

int  initialize();
char getword(int fd,char *word);
int  putword(int fd,char *word);
void imprime_resultados(int size,float tiempo[],int voltaje[]);

int main(int argc, char *argv[])
{
  int  fd,j,i[NUM];
  float tiempo[NUM];
  char c,word[128];
  clock_t c0,c1;

  //printf("\nCPU time (sec.): %f\n\n",(float)(c1-c0)/CLOCKS_PER_SEC);

  fd = initialize();

  j = 0;
  c0=clock();
  while (j<NUM)
    {
      c1=clock();
      c = getword(fd,word);
    
      i[j] = atoi(word);
      tiempo[j] = (float)(c1-c0)/CLOCKS_PER_SEC;
	
      printf("%f\t%d\n", tiempo[j], i[j]);
      j++;
      usleep(100000);       
	
    }
  imprime_resultados(NUM, tiempo, i);

  c='0'; // useless for avoiding warnings

  return 1;

}

void imprime_resultados(int size,float tiempo[],int voltaje[]){
	
	FILE *fp;
	fp=fopen("resultados.txt","a");
	fprintf(fp,"Tiempo \t Voltaje \n");  // Encabezado del archivo
	for (int i = 0; i < size; ++i){
		fprintf(fp,"%f \t\t %i \n",tiempo[i],voltaje[i]);
	}
	fclose(fp);
}

int initialize()
{
  int    fd;
  struct termios toptions;

  fd = open(MYPORT, O_RDWR | O_NOCTTY);            // open serial port
  usleep(DELAY);                                   // wait for the Arduino to reboot
  tcgetattr(fd, &toptions);                        // get current serial port settings
  cfsetispeed(&toptions, B9600);                   // set 9600 baud for input
  cfsetospeed(&toptions, B9600);                   // set 9600 baud for output

  toptions.c_cflag &= ~PARENB;                     // set no parity flag
  toptions.c_cflag &= ~CSTOPB;                     // set no stop flag
  toptions.c_cflag &= ~CSIZE;                      // set no size flag
  toptions.c_cflag |= CS8;                         // set 8 bits flag
  toptions.c_lflag |= ICANON;                      // set canonical mode
  
  tcsetattr(fd, TCSANOW, &toptions);               // commit the serial port settings

  return fd;
}

char getword(int fd,char *word)
{
  int  i;
  char buffer[1];
   
  i = 0;
  buffer[0] = '0';

  while ((buffer[0]!=' ') && (buffer[0]!='\t') && (buffer[0]!='\n'))
    {
      read(fd,buffer,1);
      *(word+i) = buffer[0];
      i++;
    }

  *(word+i) = '\0';

  return buffer[0];
}

int putword(int fd,char *word)
{
  int  i;
   
  i = 0;
  while (*word!='\0')
    {
      write(fd,word+i,1);
      i++;
    }

  return i;
}


