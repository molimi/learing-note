#
# @lc app=leetcode.cn id=1041 lang=python3
#
# [1041] 困于环中的机器人
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 机器人想要摆脱循环，在一串指令之后的状态，必须是不位于原点且方向朝北
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]         # 北 东 南 西
        rotation = 0            # R +1 L -1 rotation%4 得到方向
        x, y = 0, 0
        for ch in instructions:
            if ch == "G":
                x += directions[rotation][0]          # -1%4==3
                y += directions[rotation][1]
    
            if ch == "R":
                rotation += 1
                rotation  %= 4
            if ch == "L":
                rotation -= 1
                rotation %= 4
        return rotation != 0 or (x==0 and y ==0)            # 经过一轮循环，要么改变方向，会进入循环，或者直接回到原点
            

# @lc code=end

