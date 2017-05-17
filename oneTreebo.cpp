#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int main(){
	int M, K, TS, current_node;
	cin>>M;
	int *graph = new int[M+1];
	for (int i=1;i<M+1;i++){
		scanf("%d", &graph[i]);
	}
	bool *ts = new bool[M+1];
	graph[0] = 0;
	cin>>K;
	for(;K>0;K--){
		int q1, q2;
		scanf("%d %d", &q1, &q2);
		if(q1 == 1){
			//unordered_set<int> traversedSet;
			//TS = 0;
			for (int i=1;i<M+1;i++)
				ts[i] = false;

			current_node = q2;
			while(true){
				if(graph[current_node] == 0){
					printf("%d\n", current_node);
					break;
				}
				if(ts[graph[current_node]]){
					printf("LOOP\n");
					break;
				}
				// if(TS & 1<<graph[current_node]){
				// 	printf("LOOP\n");
				// 	break;
				// }
				// TS = TS | 1<<current_node;
				ts[current_node] = true;
				current_node = graph[current_node];
			}
		}
		else if(q1 == 2){
			graph[q2] = 0;
		}
	}
}