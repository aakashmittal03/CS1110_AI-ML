  
def check( chessBoard, r, c, N) :	
	# Check column
	for i in range(r):
		if chessBoard[i][c]==1:
			return False

	# Check diagonal 1
	for i, j in zip(range(r, -1, -1),range(c, N, 1)):
		if chessBoard[i][j]==1:
			return False

	# Check diagonal 2 
	for i, j in zip(range(r, -1, -1),range(c, -1, -1)):
		if chessBoard[i][j]==1:
			return False

	return True

def solve( chessBoard, r, N): 
	if r >= N:
		return True

	for i in range(N):
		if check(chessBoard, r, i, N) == True: 
			chessBoard[r][i] = 1
			if solve(chessBoard, r + 1, N):
				return True
			chessBoard[r][i] = 0 
	return False

        
def NQueen(N):
    chessBoard = [[0 for i in range(N+1)] for j in range(N+1)]
    solve(chessBoard, 0, N)
    display(chessBoard, N)

def display(chessBoard,N) :
    for i in range(N):
        for j in range(N):
            print(chessBoard[i][j],end=' ')
        print()

x= int(input(""))
NQueen(x)