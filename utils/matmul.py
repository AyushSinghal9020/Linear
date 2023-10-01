import numpy as np 

def convertor(val , return_val = None):

    if isinstance(val , list) or isinstance(val , np.ndarray):
    
        if return_val : 
            if isinstance(val , list): val = np.array(val)
        else : 
            if isinstance(val , np.ndarray) : val = val.tolist()
    
    else : raise ValueError(f'Cannot process inputs of type {type(val)}, pass a numpy.ndarray or python list only')

    return val

def matmul(f_row , f_col , s_row , s_col):

    if len(f_col) != len(s_row) : raise ValueError(f'Cannot multiply array with dimensions {len(f_row)}x{len(f_col)} , {len(s_row)}x{len(s_col)}')

    f_row = convertor(f_row , return_val = True)
    f_col = convertor(f_col , return_val = True)
    s_row = convertor(s_row , return_val = True)
    s_col = convertor(s_col , return_val = True)

    val = sum(f_col * s_row / 2)
    col = s_col * val

    return col
