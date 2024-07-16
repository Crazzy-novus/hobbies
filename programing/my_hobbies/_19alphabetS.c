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
    printf("\n");
}