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
}