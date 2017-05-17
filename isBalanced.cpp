#include <iostream>
#include <string>
using namespace std;

bool isBalanced(string str){
	int openB=0;
	for(int i=0;i < str.length();i++){
		if(str[i]=='(')
			openB++;
		
		else if(str[i] == ')')
			openB--;
			if(openB < 0)
				return false;
	}
	if(openB)
		return false;
	return true;
}
int fib(int n){
	switch(n){
		default:
			return fib(n-1) + fib(n-2);
		case 1:;
		case 2:;
	}
	return 1;
}
class A{
	public:
	int u,l;
	A(int i) : u(i+1), l(i){}
};
int main(){
	int v = 5;
	int x = v/0;
}
int min(int a, int b){
	return a<b?a:b;
}
int shortestPalindrome(string s) {
	int n = s.size();
	int **table = new int* [n];
	for(int i=0;i<n;i++)
		table[i] = new int[n];
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
		table[i][j]=0;
	for(int length=1;length<n;length++){
		for(int start=0;start<n;start++){
			end = start+length;
			if(s[start] == s[end])
				table[start][end] = table[start+1][end-1];
			else
				table[start][end] = min(table[l][h-1], table[l+1][h]) + 1;
		}
	}
	return table[0][n-1];
}


