import torch 
import torch.nn as nn 

class linear(nn.Module):

    def __init__(self , in_features , out_features):
        
        super().__init__()
        
        self.in_features = in_features
        self.out_features = out_features
        
        self.expected_size = 1
        
        self.layer = nn.Linear(self.in_features , self.out_features)
        
        self.in_col = torch.rand(self.in_features)
        self.out_col = torch.rand(self.out_features)
        
    def forward(self , inps):
        
        if len(inps.shape) == self.expected_size + 1:
            
            return_val = [
                mat(
                    self.in_col.detach().numpy().tolist() , 
                    val.detach().numpy().tolist() , 
                    self.in_col.detach().numpy().tolist() , 
                    self.out_col.detach().numpy().tolist()
                )[1].detach().numpy().tolist()
                for val 
                in inps]
            
            return torch.tensor(return_val)

        return_val = mat(
            self.in_col.detach().numpy().tolist() , 
            inps.detach().numpy().tolist() , 
            self.in_col.detach().numpy().tolist() , 
            self.out_col.detach().numpy().tolist()
        )[1]
        
        return return_val
