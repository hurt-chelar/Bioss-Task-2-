#include<stdio.h> 



int main()
 {  
    int n ; 
    scanf("%d",&n) ;
    int ar[n] ; 
    
    for(int i = 0 ; i<n ; i++)
    {
        scanf("%d",&ar[i]); 
    }
    int sum = 0  ; 
    for(int i = 0 ; i<n ; i++)
    {
        sum = sum + ar[i];
    }
    int x = 0 ; 
    n = (float)n ; 
    sum = (float)sum ; 
    x = (9.5*n - sum)/(0.5) ; 
    printf("%d", (int)x ) ;
    }
