class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        column={}
        boxes={}

        for i in range(9):

            row=set()

            for j in range(9):

                if board[i][j]=="." :
                    continue

                val=board[i][j]
                
                #column check 
                if j not in column:
                    column[j] = set()

                if val in column[j]:
                    return False

                column[j].add(val)
                    

                #row check       
                if val not in row:
                    row.add(val)

                elif val in row :
                    return False


                #box check
                box = (i // 3, j // 3)

                if box not in boxes:
                    boxes[box] = set()

                if val in boxes[box]:
                    return False

                boxes[box].add(val)


        return True


            