#include<stdio.h> 
int main() 
{
    int n  ;
    scanf("%d",&n);
    int arr[n] ;

    for(int i = 0 ; i < n ; i++)
    {
        scanf("%d",&arr[i]) ; 
    }
    int * a = &arr[0] ; 
    int temp = 0 ; 
    
    for(int i = 0 ; i < n ; i++)
    {
       for( int  j = i + 1 ; j< n ; j++ )
       {
           if(*(a+i)> *(a+j))
           {
               temp = *(a+i);
               *(a+i)= *(a+j) ; 
               *(a+j) = temp ;

           }
       } 
    }
    for(int i = 0 ; i < n ; i++)
    {
        printf("%d",*(a+i));
    }

    }