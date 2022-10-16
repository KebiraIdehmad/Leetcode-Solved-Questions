class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        
        cur_row = cur_col = 0
        going_up = True
        while len(res)<len(mat)*len(mat[0]):
            
            if going_up :
                
                while cur_row >= 0 and cur_col < len(mat[0]):
                    
                    res.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1
                    
                if cur_col == len(mat[0]) :
                    
                    cur_col -=1
                    cur_row +=2
                else :
                    
                    cur_row +=1
                going_up = False
            else :
                while cur_row < len(mat) and cur_col >= 0:
                                  
                    res.append(mat[cur_row][cur_col])
                    cur_row +=1
                    cur_col -=1
                if cur_row == len(mat) :
                    cur_col +=2
                    cur_row -= 1
                else:
                    cur_col +=1
                going_up = True
        return res
                                  
                    
                    
                    
                    
                    