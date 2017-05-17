#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
int max(int a, int b){
	if (a>=b)
		return a;
	return b;
}
int traverse(tree* T, char direction){
	if(T == NULL)
		return 0;
	if (direction == 'L') {
		if (T->r != NULL)
			return  max(traverse(T->r, 'R') + 1, traverse(T->l, 'L'));
		return traverse(T->l, 'L');
	}
	else if (direction == 'R'){
		if (T->l != NULL)
			return  max(traverse(T->l, 'L') +1 , traverse(T->r, 'R'));
		return traverse(T->r, 'R');
	}
}

int solution(tree * T) {
    // write your code in C++14 (g++ 6.2.0)
 	if (T == NULL)
 		return 0;
 	return max(traverse(T->l, 'L'), traverse(T->r, 'R'));   
}