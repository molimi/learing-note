#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 1024;

int weight[MAXN];

int main()
{   vector<string> results;
    int T, n;
    cin >> T;
    while(T--)
    {
        cin >> n;

        int h = log2(n+1); // 计算树的高度

        for(int i = 1; i <= n; i++)
            cin >> weight[i];

        bool exists = true;
        for(int i = 1; i <= n/2; i++)
        {
            int left = 2*i; // 左节点的编号
            int right = left + 1; // 右节点的编号
            int left_sum = 0, right_sum = 0; // 左右子树的权重和

            for(int j = 0; j < h-1; j++)
            {
                left_sum += weight[left];
                right_sum += weight[right];

                left = 2*left;
                right = 2*right+1;
            }

            if(left_sum == right_sum)
            {
                exists = false;
                break;
            }
        }

        if(exists)
            results.push_back("Yes");
        else
            results.push_back("No");
    }
    
    for (int i = 0; i<results.size(); ++i) {
        cout << results[i] << endl;
    }
    return 0;
}