#
# @lc app=leetcode.cn id=526 lang=python3
#
# [526] 优美的排列
#

# @lc code=start
class Solution:
    def countArrangement(self, n: int) -> int:
        canFill = defaultdict(list)
        for i in range(1,n+1):
            for j in range(1, n+1):
                if j % i == 0 or i % j == 0:        # 每个位置可以填入哪些数
                    canFill[i].append(j-1)

        order = sorted(canFill.keys(), key=lambda x:len(canFill[x]))    # 根据可填入数字的个数排序，优先填入个数少的
        end = (1 << n) - 1

        @lru_cache(None)
        def dfs(state):
            if state == end:                    # 全部填入
                return 1
            cnts = ans = 0
            for i in range(n):                  # 当前该填第几个位置
                if (1 << i) & state:
                    cnts += 1
            for i in canFill[order[cnts]]:      # 当前位置可以填哪些数
                if not ((1 << i) & state):      # 哪些数还没被填
                    ans += dfs(state ^ (1 << i))
            return ans
        
        return dfs(0)
# @lc code=end

