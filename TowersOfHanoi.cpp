#include<stdio.h>
int towersOfHanoi(int n,char start,char temp,char end){
	if(n==0);
	else{
		towersOfHanoi(n-1,start,end,temp); //f(n-1)
		printf("Disc %d is transferred from %c to %c\n",n,start,temp); //f(n)
		towersOfHanoi(n-1,end,temp,start); //f(n-1)
	}
}
int main(){
	int n;
	printf("Enter Number of discs: ");
	scanf("%d",&n);
	towersOfHanoi(n,'A','C','B');
}
