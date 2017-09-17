#include<stdio.h>

int fastexpo(int a,int x){
	if(x==0)return 1;
	if(x==1)return a;
	int t=fastexpo(a,x/2);
	return t*t*fastexpo(a,x&1);
}

int main(){
	int a,x;
	scanf("%d %d",&a,&x);
	printf("%d",fastexpo(a,x));
}
