#include<stdio.h>
void pattern(int);
int main()
{
    int n;
    printf("enter the value of n=");
    scanf("%d",&n);
    pattern(n);
}
void pattern(int n)
{
    int i,j,s;
// H
for(i=0;i<=n/2;i++)//1-0 
    {
        
        printf("*");
        for(s=1;s<=n;s++)//1-i
        {
            printf(" ");
        }
        printf(" *\n");   
    }
    for(i=0;i<=n+2;i++)//1-0
    {
        printf("*");
    }
    printf("\n");
    for(i=0;i<=n/2;i++)//1-0 
    {
        printf("*");
        for(s=1;s<=n;s++)//1-i
        {
            printf(" ");
        }
        printf(" *\n");   
    }
    printf("\n\n");
// A
    for(s=0;s<=n;s++)
    {
        printf(" ");
    }
    printf("*\n");
      for(i=1;i<=n/2;i++)//0-1
    {
        for(s=1;s<=n-i;s++)
        {
            printf(" ");
        }
        printf("*");
        for(s=(n-i)*2;s<=n*2;s++)
        {
            printf(" ");
        }  
        printf("*\n");
    }
    for(s=1;s<=n-3;s++)
     {
        printf(" ");
     }
     for(i=0;i<n;i++)
     {
        printf("* ");
     }
     printf("\n");
     for(i=(n/2)+2;i<=n;i++)
     {
        for(s=1;s<=n-i;s++)
        {
            printf(" ");
        }
        printf("*");
        for(s=(n-i)*2;s<=n*2;s++)
        {
            printf(" ");
        }  
        printf("*\n");
     }
     printf("\n");
// R
     for(i=0;i<=n-1;i++)//1-0
    {
        printf(" *");
    }
    printf("\n");
    for(i=0;i==0;i++)//1-0
    {
        printf(" *");
        for(s=0;s<=n+1;s++)//1-0
        {
        printf(" ");
        }
        printf("*");
    }
    printf("\n");
    for(i=0;i<=n-1;i++)//1-0
    {
        printf(" *");
    }
    printf("\n");
    for(i=0;i<=n/2;i++)//1-0
    {
        printf(" *");
        for(s=n-i;s<=n-1;s++)
        {
            printf("  ");
        }
        printf("  *\n");
    }
    printf("\n");
//S
    for(i=1;i<=n;i++)
    {
        printf(" *");
    }
    printf("\n");
    printf(" *");
    for(s=0;s<=n;s++)
    {
        printf(" ");
    }
    printf("\n");
    for(i=1;i<=n;i++)
    {
        printf(" *");
    }
    printf("\n  ");
    for(s=0;s<=n;s++)
    {
        printf(" ");
    }
    printf(" *\n");
    for(i=1;i<=n;i++)
    {
        printf(" *");
    }
    printf("\n\n");
// H
    for(i=0;i<=n/2;i++)//1-0 
    {
        printf("*");
        for(s=1;s<=n;s++)//1-i
        {
            printf(" ");
        }
        printf(" *\n");   
    }
    for(i=0;i<=n+2;i++)//1-0
    {
        printf("*");
    }
    printf("\n");
    for(i=0;i<=n/2;i++)//1-0 
    {
        printf("*");
        for(s=1;s<=n;s++)//1-i
        {
            printf(" ");
        }
        printf(" *\n");   
    }
    printf("\n");
// A
    for(s=0;s<=n;s++)
    {
        printf(" ");
    }
    printf("*\n");
      for(i=1;i<=n/2;i++)//0-1
    {
        for(s=1;s<=n-i;s++)
        {
            printf(" ");
        }
        printf("*");
        for(s=(n-i)*2;s<=n*2;s++)
        {
            printf(" ");
        }  
        printf("*\n");
    }
    for(s=1;s<=n-3;s++)
     {
        printf(" ");
     }
     for(i=0;i<n;i++)
     {
        printf("* ");
     }
     printf("\n");
     for(i=(n/2)+2;i<=n;i++)
     {
        for(s=1;s<=n-i;s++)
        {
            printf(" ");
        }
        printf("*");
        for(s=(n-i)*2;s<=n*2;s++)
        {
            printf(" ");
        }  
        printf("*\n");
     }
     printf("\n");
}
/* T
    for(i=1;i<=n;i++)
    {
     printf("**");
    }
    printf("\n");
    for(j=1;j<=n-1;j++)
    {
        for(s=1;s<=n/2;s++)
        {
         printf("  ");
        }
        printf("*\n");
    }
    printf("\n");
// H
for(i=0;i<=n/2;i++)//1-0 
    {
        printf("*");
        for(s=1;s<=n;s++)//1-i
        {
            printf(" ");
        }
        printf(" *\n");   
    }
    for(i=0;i<=n+2;i++)//1-0
    {
        printf("*");
    }
    printf("\n");
    for(i=0;i<=n/2;i++)//1-0 
    {
        printf("*");
        for(s=1;s<=n;s++)//1-i
        {
            printf(" ");
        }
        printf(" *\n");   
    }
}*/