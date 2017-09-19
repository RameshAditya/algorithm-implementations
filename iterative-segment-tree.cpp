#include<stdio.h>

/*const int n=16;
int t[2*n]={0};

void build() {  // build the tree
  for (int i = n - 1; i > 0; i--) t[i] = t[i<<1] + t[i<<1|1];
}

void modify(int p, int value) {  // set value at position p
  for (t[p += n] = value; p > 1; p >>= 1) t[p>>1] = t[p] + t[p^1];
}

int query(int l, int r) {  // sum on interval [l, r)
  int res = 0;
  for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
    if (l&1) res += t[l++];
    if (r&1) res += t[--r];
  }
  return res;
}
*/




const int n=8;
int t[2*n]={0};

void build(){
	for(int i=n-1;i>0;--i)t[i]=t[i<<1]+t[i<<1|1];
}

void update(int ind,int val){
	for(t[ind+=n]=val;ind>1;ind>>=1)t[ind>>1]=t[ind]+t[ind^1];
}
void query(int l,int r){
	int res=0;
	for(l+=n,r+=n;l<r;l>>=1,r>>=1){
		if(l&1)res+=t[l++];
		if(r&1)res+=t[--r];
	}
	printf("\n%d\n",res);
}


int main(){
	int i;
	for(i=n;i<2*n;i++)t[i]=i-n+1;
	build();
	for(i=0;i<2*n;i++)printf("%d ",t[i]);
	query(0,8);
	

}


