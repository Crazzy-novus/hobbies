#include<stdio.h>
int main()
{
    int arr[100],n;
    int i,j,result=0,tem;
    printf("enter the value of n:");
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        printf("enter the element :%d:\n",i+1);
        scanf("%d",&arr[i]);
    }
     
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(arr[i]>arr[j])
            {
                tem=arr[i];
                arr[i]=arr[j];
                arr[j]=tem;
            }
        }

    }
 /*printing array*/      
 for(int i=0;i<n;i++)
    {
        
        printf(" %d,",arr[i]);
    }
   //implimintation
    for(i=n-1;i>-1;i--)
    {
    	if(arr[i]-1==arr[i-1])
        {
            result = result + arr[i];
            i--;
        }
        else
        {
            result = result + arr[i];
        }
    }
     printf("answer is %d\n",result);
return 0;
}