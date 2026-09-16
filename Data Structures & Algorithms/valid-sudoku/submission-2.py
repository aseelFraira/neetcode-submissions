class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for val in row:
                if val != "." and val in seen:
                    return False
                seen.add(val)
        
        for col in range(9):
            seen = set()
            for row in range(9):
                val = board[row][col]
                if val != '.' and val in seen:
                    return False
                seen.add(val)
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()

                for row in range(3):
                    for col in range(3):
                        val = board[box_row + row][box_col + col]

                        if val != ".":
                            if val in seen:
                                return False
                            seen.add(val)

        return True
        


        
        

        