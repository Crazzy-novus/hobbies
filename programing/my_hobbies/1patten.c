#include<stdio.h>
int main()
{
    int n,i,space,j;
    printf("enter the number");
    scanf("%d",&n);
  for(i=1;i<=n;i++)
    {
        for(space=1;space<=n-i;space++)
        {
         printf(" ");
        }
         for(j=1;j<=i;j++)
        {
            printf(" *");
        }
        
        printf("\n");

    }
    for(i=n-1;i>=0;i--)
      {
          for(space=0;space<n-i;space++)
           {
            printf(" ");
           }


          for(j=1;j<=i;j++)
          {
          printf(" *");
      }
      printf("\n");
      }

}
