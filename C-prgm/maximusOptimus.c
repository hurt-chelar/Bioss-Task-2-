#include<stdio.h> 
int max(int arr[3])
    {
        
        int max = 0 ; 
        max = arr[0];
        for(int i = 0 ; i < 3 ; i++)
        {
            if(max < arr[i])
            {
                max = arr[i] ;
                 
            }
        }
        return max ; 
    }
int main() 
{
    int arr[3] ; 
    for(int i = 0 ; i <3; i++ )
    {
        scanf("%d",&arr[i]) ; 
    }
    int n ; 
    scanf("%d",&n); 

    int sum = 0 ; 
    
    for(int j = 0; j<n ; j++)
    {
    for(int i = 0 ; i<3 ; i++)
    {
        int maximum = max(arr) ; 
        if(arr[i]==maximum)
        {
            sum = sum + maximum ; 
            arr[i]= arr[i]-1 ; 
            break ;  
        }
    }
    }

    // for(int i = 0 ; i<3 ; i++)
    // {
    //     printf("%d",arr[i]);
    // } 
    printf("%d", sum) ; 
    

}