#include<math.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define  C     5       // numero de columnas totales
#define  M     1024    // cantidada de niveles del Arduino
#define  tau   0.2     // intervalo de sampleo del Arduino

int histo(double *y,int *x,int h, int c);

int main(int argc, char *argv[])
{
  int    c,h,i,n,*x;
  char   filename[100],number[100];
  double *y;
  FILE   *fp;

  strcpy(filename,argv[1]);

  if (argc!=2) printf("\nSomething is wrong or nothing to do.\n\n");
  else
    {  h=0;

       fp=fopen(filename,"r");
       while (fscanf(fp,"%d",&n)==1) h++;
       fclose(fp);

       x = (int *)malloc(h*sizeof(int));
       y = (double *)malloc((M+1)*sizeof(double));

       h = 0;
       fp=fopen(filename,"r");
       while (fscanf(fp,"%d",&n)==1) 
           {
             *(x+h)=n;
             h++;
           }
       fclose(fp);

       h = h/C;

       for (c=1;c<C;c++)
          {
            sprintf(number,"%d",c);
            histo(y,x,h,c);
            strcpy(filename,"histo_");
            strcat(filename,number);
            strcat(filename,".dat"); printf("%s\n",filename);

            fp=fopen(filename,"w");
            for (i=1;i<M+1;i++) fprintf(fp,"%d\t%f\n",i,*(y+i));
            fclose(fp);

          }

       free(x);
       free(y);

    }

  return 1;
}

int histo(double *y,int *x,int h, int c)
{
   int i,j;

   for (i=0;i<M+1;i++) *(y+i) = 0.0;

   for (i=0;i<h;i++)
      {
        j=(*(x+C*i+c));
        *(y+j) += 1.0/(double)h;
      }

   return 1;
}


