class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        rows_cols=[]
        res=[]
        cur_col = cur_row =0
        going_right = True
        going_up = False
        going_down = False
        goin_left = False
        while len(res)< len(mat)*len(mat[0]):
            if going_right :
                while cur_col < len(mat[0]) and [cur_row,cur_col] not in rows_cols:
                    res.append(mat[cur_row][cur_col])
                    rows_cols.append([cur_row,cur_col])
                    cur_col +=1
                cur_col -=1
                cur_row +=1
                going_down = True
                going_right = False
            if going_down :
                while cur_row < len(mat) and [cur_row,cur_col] not in rows_cols:
                    res.append(mat[cur_row][cur_col])
                    rows_cols.append([cur_row,cur_col])
                    cur_row +=1
                cur_row -=1
                cur_col -=1
                going_down = False
                going_left = True
            if going_left :
                while cur_col >= 0 and [cur_row,cur_col] not in rows_cols:
                    res.append(mat[cur_row][cur_col])
                    rows_cols.append([cur_row,cur_col])
                    cur_col -=1
                cur_col += 1
                cur_row -=1
                going_left = False
                going_up = True
            if going_up :
                while cur_row >= 0 and [cur_row,cur_col] not in rows_cols:
                    res.append(mat[cur_row][cur_col])
                    rows_cols.append([cur_row,cur_col])
                    cur_row -=1
                cur_col += 1
                cur_row +=1
                going_up = False
                going_right = True
        return res
			    	        
	    




