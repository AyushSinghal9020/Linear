import torch

def matmul(arr : Tuple , arr_ : Tuple) -> torch.tensor : 
    
    f_row = arr[0]
    f_col = arr[1]

    s_row = arr[0]
    s_col = arr[1]

    if f_col != s_row: raise ValueError('Matrices with shape (' , f_row , 'x' , f_col , ') and (' , s_row , 'x' , s_col , 'cannot be multiplied')
    else :
            
        first_elem = sum([
            f_row[0] * f_col[s_index] * s_col[0] * s_row[f_index]
            for f_index , s_index 
            in zip(range(f_row.shape[0]) , range(s_row.shape[0]))])

        mat = torch.empty((f_row.shape[0] , s_row.shape[0]))

        mat[0][0] = first_elem

        for f_index in range(s_row.shape[0]):

            for s_index in range(f_row.shape[0]):

                mat[s_index][f_index] = first_elem / s_col[0] * f_row[f_index] * s_col[s_index]
                
        return mat
