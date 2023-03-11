class Solution:
    def totalFruit(self, fruits) -> int:
        slow, fast = 0, 0
        max_len = 1
        lt = []
        while fast < len(fruits):
            lt.append(fruits[fast])
            while len(set(lt)) > 2:
                lt.remove(fruits[slow])
                slow += 1
            max_len = max(max_len, fast-slow+1)
            fast += 1
        return max_len
    

if __name__ == '__main__':
    solution = Solution()
    print(solution.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))