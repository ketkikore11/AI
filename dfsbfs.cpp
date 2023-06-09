#include <iostream>
#include <list>
#include <map>
#include <queue>
using namespace std;

class Graph{
  public:
  
  map<int,list<int> >adjList;
  map<int,bool>visited;
  queue<int> q;
  
  void addEdge(int start, int dest){
    adjList[start].push_back(dest);
    adjList[dest].push_back(start);
  }
  
  void dfs(int a){
    visited[a]=true;
    cout<<a<<" ";
    for(int i:adjList[a]){
      if(!visited[i]){
        dfs(i);
        }
      }
  }

  void bfs(){
    if(q.empty()){
      return;
    }
    int n=q.front();
    q.pop();
    cout<<n<<" ";
    for(int i:adjList[n]){
      if(!visited[i]){
        visited[i]=true;
        q.push(i);
        }
      }
    bfs();
  }
};

int main(){
  
  Graph g;
  int n,e;
  cout<<"Enter total number of nodes: ";
  cin>>n;
  cout<<"Enter total number of edges: ";
  cin>>e;
  int u,v;
  cout<<"Enter edges (First start node then destination node, separated by enter key):- "<<endl;
  for(int i=0;i<e;i++){
    cout<<"Enter edge: ";
    cin>>u;
    cin>>v;
    g.addEdge(u,v);
  }
  
  int x;
  cout<<endl;
  cout<<"Enter 1 to implement DFS and 2 to implement BFS: ";
  cin>>x;
  if(x==1){
    cout<<"Path for DFS: ";
    g.dfs(0);
    cout<<endl;
  }
  else if(x==2){
    cout<<"Path for BFS: ";
    g.q.push(0);
    g.visited[0]=true;
    g.bfs();
    cout<<endl;
  }
  else{
    cout<<"Incorrect option entered";
  }
  return 0;
}

//output
/*
Enter total number of nodes: 5
Enter total number of edges: 6
Enter edges (First start node then destination node, separated by enter key):-
Enter edge: 0
1
Enter edge: 0
2
Enter edge: 1
2
Enter edge: 1
3
Enter edge: 2
4
Enter edge: 3
4

Enter 1 to implement DFS and 2 to implement BFS: 1
Path for DFS: 0 1 2 4 3
*/
