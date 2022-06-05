#include<stdio.h>
int main()
{
    int i = 0 ; 
    char str1[100] ; 
    char str2[100] ;
    int cnt1= 0 ; 
    int cnt2= 0 ; 
    gets(str1) ;
    gets(str2) ; 
    for (i = 0; str1[i] != '\0'; ++i)
    {
        cnt1++ ; 
    }
    for (i = 0; str2[i] != '\0'; ++i)
    {
        cnt2++ ; 
    }
    if(cnt1==cnt2)
    {
        printf("Equal");
    }
    else
    {
        if(cnt1>cnt2)
        {
            printf("Second is Shorter");
        }
        else
        {
            printf("First is Shorter") ; 
        }
    }
    
} 