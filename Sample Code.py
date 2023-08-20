import torch.nn as nn 
import torch

class linear(nn.Module):

    def formula(self , val_1 , val_2): return torch.sin(val_1) * torch.sqrt(1 - torch.square(val_2))

    def merge(self , in_features , out_features):

        par = torch.empty(
            (out_features.shape[0] , in_features.shape[0]))

        for row in range(out_features.shape[0]):

            for col in range(in_features.shape[0]):

                val_1 = out_features[row]
                val_2 = in_features[col]

                par[row][col] = self.formula(val_1 , val_2)

        par = nn.Parameter(par)

        return par
    
    
    def __init__(self , in_features , out_features):
        
        super().__init__()
        
        self.in_features = in_features
        self.out_features = out_features
        
        self.layer = nn.Linear(self.in_features , self.out_features)
        
        self.in_col = torch.rand(self.in_features)
        self.out_col = torch.rand(self.out_features)
        
        self.parameter = self.merge(self.in_col , self.out_col)
        
        self.layer.weight = self.parameter
        
#     def __call__(self , in_features , out_features):return self.layer
    
    def forward(self , inps):
        return self.layer(inps)
    
#     def weight(self): return self.layer.parameters
