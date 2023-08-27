import torch

def matmul(arr : tuple , arr_ : tuple) -> torch.tensor : 
    
    f_row = arr[0]
    f_col = arr[1]

    s_row = arr_[0]
    s_col = arr_[1]
    
    if type(f_row) != torch.tensor: torch.tensor(f_row)
    if type(f_col) != torch.tensor: torch.tensor(f_col)
    if type(s_row) != torch.tensor: torch.tensor(s_row)
    if type(s_col) != torch.tensor: torch.tensor(s_col)
    
    if f_col.shape[0] != s_row.shape[0]: raise ValueError('Matrices with shape (' , f_row , 'x' , f_col , ') and (' , s_row , 'x' , s_col , 'cannot be multiplied')
    else :
            
        val =sum([
            (f_col[index] * s_row[index]) / 2
            for index
            in range(f_row.shape[0])])

        row = [
            s_row[index] * val
            for index 
            in range(s_row.shape[0])]

        col = [
            s_col[index] * 2
            for index 
            in range(s_col.shape[0])]

        return torch.concat([torch.tensor(row) , torch.tensor(col)])
