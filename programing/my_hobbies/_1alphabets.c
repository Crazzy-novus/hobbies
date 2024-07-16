#include<stdio.h>
void pattern(int);
int main()
{
    int n;
    printf("enter the value of n=");
    scanf("%d",&n);
    pattern(n);
}
//function definition
void pattern(int n)
{
    int i,j,s;
    for(s=0;s<=n;s++)
    {
        printf(" ");
    }
    printf("*\n");
    for(i=1;i<=n/2;i++)
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
}