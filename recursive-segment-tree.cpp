#include<bits/stdc++.h>

using namespace std;

int tree[21];
int A[10];

void build(int node, int start, int end){
	if(start==end)
		tree[node]=A[start];
	else{
		int mid=(start+end)/2;
		build(2*node,start,mid);
		build(2*node+1,mid+1,end);
		tree[node]=tree[2*node]+tree[2*node+1];
	}
}

void update(int node, int start, int end, int val, int idx){
	if(start==end){
		tree[node]+=val;
		A[idx]+=val;
	}
	else{
		int mid=(start+end)/2;
		if(start<=idx && idx<=mid)
			update(2*node,start,mid,val,idx);
		else
			update(2*node+1,mid+1,end,val,idx);
		
	tree[node]=tree[2*node]+tree[2*node+1];	
	}
}

int query(int node,int start,int end,int l, int r){
	if(r<start||l>end)return 0;
	if(l<=start && r>=end)
		return tree[node];
	int mid=(start+end)/2;
	int p1=query(2*node,start,mid,l,r);
	int p2=query(2*node+1,mid+1,end,l,r);
	return (p1+p2);
}

int main(){
	int n;
	scanf("%d",&n);
	
	for(int i=0;i<n;i++)scanf("%d",&A[i]);
	int q;
	build(1,0,n-1);
	scanf("%d",&q);
	while(q--){
		int l,r;
		scanf("%d%d",&l,&r);
		printf("%d\n",query(1,0,n-1,l-1,r-1));
	}
}

void build(int node,int start, int end){
	if(start==end)tree[node]=A[start];
	else{
		int mid=(start+end)/2;
		build(node<<1,start,mid);
		build(node<<1|1,mid+1,end);
		tree[node]=tree[node<<1]+tree[node<<1|1];
	}
}

void update(int node,int start, int end,int val, int idx){
	if(start==end){
		tree[node]+=val;
		A[idx]+=val;
	}
	else{
		int mid=(start+end)/2;
		if(start<=idx && idx<=mid)
			update(node<<1,start,mid,val,idx);
		else
			update(node<<1|1,mid+1,end,val,idx);
		tree[node]=tree[node<<1]+tree[node<<1|1];
	}
}
