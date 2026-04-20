class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        sol = [[] for _ in range(1, 10)] # for checking grid

        for i in range(1, 10):
            sol1 = [] # for checking the rows
            sol2 = [] # for checking the cols
            for j in range(1, 10):
                
                # 1. row checking (yes i comment my code I am not ai :)
                val_row = board[i-1][j-1]
                if val_row != ".":
                    if val_row not in sol1:
                        sol1.append(val_row)
                    else:
                        return False

                # 2. col checking
                val_col = board[j-1][i-1]
                if val_col != ".":
                    if val_col not in sol2:
                        sol2.append(val_col)
                    else:
                        return False

                #3. For the square 3x3 grid
                if val_row != ".":
                    key = ((i-1)//3) + 3 * ((j-1)//3) + 1
                    if val_row not in sol[key-1]:
                        sol[key-1].append(val_row)

                    else:
                        return False
                
        return True