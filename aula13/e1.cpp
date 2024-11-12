#include <iostream>
#include <vector>
using namespace std;

void dfs(int node, vector<vector<int>>& graph, vector<int>& visited) {
    visited[node] = 1;

    for (int elem : graph[node]) {
        if (visited[elem] == 0) {
            dfs(elem, graph, visited);
        }
    }
}

void morning_walk(int V, int E) {
    vector<int> degrees(V, 0);
    vector<vector<int>> graph(V);
    vector<int> visited(V, 1);

    if (E == 0) {
        cout << "Not Possible" << endl;
        return;
    }

    for (int i = 0; i < E; ++i) {
        int u, v;
        cin >> u >> v;
        degrees[u] += 1;
        degrees[v] += 1;
        graph[u].push_back(v);
        graph[v].push_back(u);
        visited[u] = 0;
        visited[v] = 0;
    }

    for (int i = 0; i < V; ++i) {
        if (degrees[i] % 2 == 1) {
            cout << "Not Possible" << endl;
            return;
        }
    }

    bool resp = false;
    for (int i = 0; i < V; ++i) {
        if (visited[i] == 0) {
            dfs(i, graph, visited);

            for (int elem : visited) {
                if (elem == 0) {
                    cout << "Not Possible" << endl;
                    return;
                }
            }

            cout << "Possible" << endl;
            return;
        }
    }
}

int main() {
    string line;
    while (getline(cin, line)) {
        if (line.empty()) {
            continue;
        }

        int V, E;
        sscanf(line.c_str(), "%d %d", &V, &E);

        morning_walk(V, E);
    }

    return 0;
}
