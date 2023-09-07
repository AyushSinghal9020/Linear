cdef tuple matmul(list f_row , list f_col , list s_row , list s_col):
    
    row = [0] * len(s_row)
    col = [0] * len(f_col)
    
    val = 0
    
    val = sum([
        f_col[index] * s_row[index] / 2
        for index 
        in range(len(f_col))
    ])

    row = [
        f_row[index] * val 
        for index 
        in range(len(f_col))
    ]
    col = np.array([
        s_col[index] * 2
        for index
        in range(len(s_col))
    ])
    
    return (row , col)
