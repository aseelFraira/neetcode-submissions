class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        const int INF = 2147483647;
        int n = grid.size();
        int m = grid[0].size();
        queue<pair<int, int>> q; // changed from stack to queue for BFS

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 0) {
                    q.push({i, j});
                }
            }
        }

        vector<pair<int, int>> directions = {
            {1, 0}, {-1, 0}, {0, 1}, {0, -1}
        };

        while (!q.empty()) {
            pair<int, int> p = q.front();
            int x = p.first;
            int y = p.second;
            q.pop();

            for (auto [dx, dy] : directions) {
                int nx = x + dx;
                int ny = y + dy;

                if (nx >= 0 && ny >= 0 && nx < n && ny < m) {
                    if (grid[nx][ny] == INF) {
                        grid[nx][ny] = grid[x][y] + 1;
                        q.push({nx, ny});
                    }
                }
            }
        }
    }
};
