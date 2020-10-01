#include<bits/stdc++.h>
using namespace std;

int main(){
	int A[] = {1, 3, 4, 6, 8, 9};
	int n = 6;
	//Accumulate: sum(base address, end, initial_value)
	cout<<"Total sum: "<<accumulate(A,A+n,0)<<"\n";
	int B[n+2];
	B[0] = 0;
	//partial_sum: prefix_sum(base address, end, address to store in)
	partial_sum(A, A+n, B+1);
	cout<<"Prefix sum: ";
	for(auto i:B)cout<<i<<" "; cout<<"\n";	
	int da[n];
	adjacent_difference(A,A+n,da);
	cout<<"Difference array: ";
	for(auto i:da)cout<<i<<" ";
}
