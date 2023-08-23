def matmul(x , y , a , b):
    
    u = sum([
        x[0] * y[ind] * b[0] * a[index]
        for index , ind 
        in zip(range(x.shape[0]) , range(a.shape[0]))])

    samp = torch.empty((x.shape[0] , a.shape[0]))

    samp[0][0] = u

    for ind in range(a.shape[0]):

        for index in range(x.shape[0]):

            samp[index][ind] = u / b[0] * x[ind] * b[index]
            
    return samp
