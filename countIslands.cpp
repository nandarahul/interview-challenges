#include <iostream>
#include <queue>
#include <utility>
using namespace std;

int BFS(int** &Mat, int i, int j, int m, int n, int LABEL){
	if(Mat[i][j] == LABEL || Mat[i][j] == 0)
		return 0;
	queue<pair<int,int> > Q;
	pair<int,int> P(i,j);
	Q.push(P);
	Mat[i][j] = LABEL;
	while(!Q.empty()){
		pair<int,int> F = Q.front();
		if(F.first < m-1 && Mat[F.first + 1][F.second]!=0 && Mat[F.first + 1][F.second]!=LABEL){
			pair<int,int> neighbour(F.first+1, F.second);
			Q.push(neighbour);
			Mat[neighbour.first][neighbour.second] = LABEL;
		}
		if(F.second < n-1 && Mat[F.first][F.second+1]!=0 && Mat[F.first][F.second + 1]!=LABEL){
			pair<int,int> neighbour(F.first, F.second+1);
			Q.push(neighbour);
			Mat[neighbour.first][neighbour.second] = LABEL;
		}
		if(F.first > 0 && Mat[F.first - 1][F.second]!=0 && Mat[F.first - 1][F.second]!=LABEL){
			pair<int,int> neighbour(F.first-1, F.second);
			Q.push(neighbour);
			Mat[neighbour.first][neighbour.second] = LABEL;
		}
		if(F.second > 0 && Mat[F.first][F.second-1] != 0 && Mat[F.first][F.second - 1] != LABEL){
			pair<int,int> neighbour(F.first, F.second-1);
			Q.push(neighbour);
			Mat[neighbour.first][neighbour.second] = LABEL;
		}
		Q.pop();
	}
	return 1;

}

int countIslands(int** &Mat, int m, int n){
	if(m<=0 || n<=0)
		return 0;
	int count = 0, LABEL= -1;
	for(int i=0;i<m;i++)
		for(int j=0;j<n;j++)
			count += BFS(Mat, i, j, m ,n, LABEL);

	return count;
}

int main(int argc, char const *argv[])
{
	int **Mat, m, n;
	cin>>m>>n;
	Mat = new int*[m];
	for(int i=0;i<m;i++)
		Mat[i] = new int[n];
	for(int i=0;i<m;i++){
		for(int j=0;j<n;j++)
			cin>>Mat[i][j];
	}
	cout<<"No. of Islands:"<<countIslands(Mat, m, n)<<"\n";
}