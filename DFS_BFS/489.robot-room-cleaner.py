#
# @lc app=leetcode id=489 lang=python3
#
# [489] Robot Room Cleaner
#

# @lc code=start
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # up/left/down/right -> 0/1/2/3
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        visited = set()
        def dfs(pos=(0,0),d=0):
            visited.add(pos)
            robot.clean()
            for i in range(4):
                new_d = (d+i)%4
                new_pos = (pos[0] + directions[new_d][0],\
                            pos[1] + directions[new_d][1])
                if new_pos not in visited and robot.move():
                    dfs(new_pos,new_d)
                    go_back()
                robot.turnRight()
        
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        dfs()
# @lc code=end

