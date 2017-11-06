class Solution(object):
    def islandPerimeter(self, grid):
        s = 0
        if not grid:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    # print (s)
                    s+=4
                    if i>0 and grid[i-1][j]==1:

                        s=s-2
                    if j>0 and grid[i][j-1]==1:

                        s=s-2
        return (s)