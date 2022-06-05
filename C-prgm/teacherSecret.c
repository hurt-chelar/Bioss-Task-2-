#include<stdio.h>
#include<string.h> 



int find_string(char str[], char search[] )
{
int i = 0, j = 0 ;
for (i = 0 ; str[i]!='\0' && search[j]!='\0'; i++)
{
    if(search[j]==str[i])
        {
            j++ ;
        }
    else
    {
        j = 0 ;
    }

}

if(j==strlen(search))
    return 1 ;
else
    return 0 ;
}


int main() 
{ 
    int n ; 
    scanf("%d",&n) ;
    // printf("%d",n) ;

    char word[n][20]; 
	for(int i=0;i<n;i++) 
	{ 
		scanf("%s",word[i]); 
	} 
    // for(int i=0;i<n;i++) 
	// { 
	// 	printf("%s",word[i]); 
	// } 




    int key1[n]  ; 
    int j ; 
    for(j = 0 ; j<n ; j++)
    {
        scanf("%d",&key1[j]) ; 
    }

    // for(j = 0 ; j<n ; j++)
    // {
    //     printf("%d",key1[j]) ; 
    // }
  
    // for(int i = 0 ; i<n ; i++)
    // {
    //     printf("%d",key[i]) ; 
    // }

    char answer[100];
    scanf("\n"); 
    scanf("%[^\n]s",answer);

    // printf("string is: %s\n", answer);


    int x=0 ; 
    int ctrl = 0 ;
    int sum = 0 ;  
    for(int i = 0 ; i<n ; i++)
    {
        x =find_string(answer,word[i]);
        if(x==1)
        {
            ctrl = ctrl + 1 ; 
            sum = sum + key1[i] ; 
        }
    } 
    printf("%d",sum) ; 
}