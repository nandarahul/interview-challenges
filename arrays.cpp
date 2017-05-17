#include <iostream>
#include <vector>
#include <fstream>
using namespace std;


//Find the sum of the absolute difference of every pair of elements in a sorted array of numbers.
#include <queue>
#include <utility>

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
		for(int j=0;j<n;j++){
			//cout<<i<<" "<<j<<" "<<Mat[i][j]<<" ";
			int b = BFS(Mat, i, j, m ,n, LABEL);
			//cout<<"BFS:"<<b<<"\n";
			count += b;}

	return count;
}



int sumAbsDiff(vector<int> data){
	int sum = 0;
	for(int i=0;i<data.size();i++)
		sum += i*data[i] - (data.size()-i-1)*data[i];
	return sum;
}
void callSumAbsDiff(){
	int m[] = {1,3,5};
	std::vector<int> v(m, m+3);
	int q = v.front();
	cout<<q<<"\n";
	cout<<sumAbsDiff(v)<<"\n";
}

int binarySearch(vector<int> &A, int low, int high, int val){
	if(low > high) return -1;
	int mid = (low+high)/2;
	if(A[mid]==val) return mid;
	if(A[low]<=val && A[mid-1]>=val)
		return binarySearch(A, low, mid-1, val);
	return binarySearch(A, mid+1, high, val);
}

int checkSortedSubArray(std::vector<int> &A, int low, int high){
	if(low > high) return false;
	return A[low] <= A[high];
}

int searchRotatedSortedArray(vector<int> &A, int low, int high, int val){
	if(low > high) return -1;
	int mid = (low+high)/2;
	if(A[mid]==val) return mid;
	if(checkSortedSubArray(A, low, mid-1))
		if(A[low]<=val && val<=A[mid-1])
			return binarySearch(A, low, mid-1, val);
		else
			return searchRotatedSortedArray(A, mid+1, high, val);
	else if(checkSortedSubArray(A, mid+1, high))
		if(A[mid+1]<=val && val<=A[high])
			return binarySearch(A, mid+1, high, val);
		else
			return searchRotatedSortedArray(A, low, mid-1, val);
	return -1;

}

void swap(int &a, int &b){
	int temp = a;
	a = b;
	b = temp;
}
int partition(vector<int> &A, int low, int high){
	int pivotIndex = high;
	int i=low;
	for(int j=low;j<=high-1;j++){
		if(A[j]<A[pivotIndex]){
			swap(A[i], A[j]);
			i++;
		}
	}
	swap(A[i], A[pivotIndex]);
	return i;
}

void quickSort(vector<int> &A, int low, int high){
	if(low < high){
		int pivotIndex = partition(A, low, high);
		quickSort(A, low, pivotIndex-1);
		quickSort(A, pivotIndex+1, high);
	}
}


int longestPalindrome(int n, string s) {
    bool ** table = new bool* [n];
    for(int i=0;i<n;i++)
    	table[i] = new bool[n];
    int maxLength = 1;
    for(int i=0;i<n;i++)
    	table[i][i] = true;
    for(int i=0;i<n-1;i++){
    	if(s[i] == s[i+1]){
    		table[i][i+1] = true;
    		maxLength = 2;
    	}
    }
    for(int length=3;length<=n;length++){
    	for(int i=0;i < n-length-1;i++){
    		int j = i+length-1;
    		if(table[i+1][j-1] && s[i] == s[j]){
    			table[i][j] = true;
    			if(length>maxLength)
    				maxLength = length;
    		}
    		else
    			table[i][j] = false;
    	}
    }

    return maxLength;
}


int main(int argc, char const *argv[])
{
	// int **Mat, m, n;
	// cin>>m>>n;
	// Mat = new int*[m];
	// for(int i=0;i<m;i++)
	// 	Mat[i] = new int[n];
	// for(int i=0;i<m;i++){
	// 	for(int j=0;j<n;j++)
	// 		cin>>Mat[i][j];
	// 	//cout<<"\n";
	// }
	// cout<<"No. of Islands:"<<countIslands(Mat, m, n)<<"\n";
	string s = "aabbefbbaa";
	cout<<longestPalindrome(10, s);
	

}