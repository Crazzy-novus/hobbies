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

}