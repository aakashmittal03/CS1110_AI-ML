import numpy as np
s=[]
print("Replace the Blank space with 0")

for i in range(9):
  r=list(input("enter the row {} elements of the problem sudoku(without spaces and commas):".format(i+1)))
  r=[int(i) for i in r]
  s.append(r)
print("The Input Matrix is:",np.matrix(s))

def possible(y,x,n):
    global suduko
    for i in range(0,9):
        if s[y][i] == n:
            return False
    for i in range(0,9):
        if s[i][x] == n:
            return False
    box_y = (y//3)*3
    box_x = (x//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if s[box_y+i][box_x+j]==n:
                return False
    return True
def solve():
    for y in range(0,9):
        for x in range(0,9):
            if s[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        s[y][x] = n
                        solve()
                        s[y][x] = 0
                return
    print(np.matrix(s))
solve()