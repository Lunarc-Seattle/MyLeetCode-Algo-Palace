class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                if val in row[r]:
                    return False
                row[r].add(val)

                if val in col[c]:
                    return False
                col[c].add(val)

                box_index = (r//3)*3+(c//3)
                if val in box[box_index]:
                    return False
                box[box_index].add(val)

        return True
                
            
                
        
