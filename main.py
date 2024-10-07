import numpy as np
import matplotlib.pyplot as plt

#Number validator
def is_valid(x, y, n, grid):

    #Check lines
    for i in range(9):
        if(grid[y][i]==n): return False
        if(grid[i][x]==n): return False

    #Grid coordinates
    _x = (x//3)*3
    _y = (y//3)*3

    #Check grid
    for grid_y in range(3):
        for grid_x in range(3):
            if(grid[_y+grid_y][_x+grid_x])==n: return False

    return True


#Solver
def solve(grid):
    for y in range(9):
        for x in range(9):
            if(grid[y][x]==0):
                for n in range(1,10):
                    if(is_valid(x,y,n,grid)):
                        grid[y][x]=n
                        if(solve(grid)):
                            return True
                        grid[y][x]=0

                #If there are no known possible solutions, return False
                return False
    return True


#Main
if __name__ == "__main__":

    #Sample Test Problem
    grid=[[6,0,7,0,3,1,0,0,4],
          [0,0,3,0,4,0,2,0,0],
          [0,9,0,8,0,0,0,0,0],
          [4,0,0,9,0,0,0,7,8],
          [7,0,0,0,0,0,0,0,0],
          [0,0,2,0,0,4,0,0,0],
          [1,0,0,0,0,0,0,0,0],
          [0,6,0,0,0,0,0,4,0],
          [0,4,8,7,0,0,1,0,6]]
    
    solve(grid)
    print(np.matrix(grid))