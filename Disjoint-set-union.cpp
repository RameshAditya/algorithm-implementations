#include<bits/stdc++.h>
using namespace std;
int par[10];

//Union-Find in 2 lines
int find(int x){par[x]==x?x:find(par[x]);}
int merge(int x,int y){par[find(x)]=find(y);}

int find(int x){par[x]==x?x:find(par[x]);}
int merge(int x, int y){par[find(x)] = find(y);}

int main(){
	for(int i=0;i<10;i++)par[i]=i;
	merge(3,4);
	merge(4,5);
	for(int i=0;i<10;i++)printf("%d ",find(i));
}
