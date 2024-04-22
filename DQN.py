import torch 
import torch.nn as nn

class DQN(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(DQN, self).__init__()
        self.layer1 = nn.Linear(state_dim, 128) # first layer - takes inputs of size state_dim and outputs 128 features
        self.layer2 = nn.Linear(128, 128) # second layer - takes 128 features and outputs another 128 features
        self.layer3 = nn.Linear(128, action_dim) # third layer - transfroms 128 features into outputs corresponding to the Q-values of each possible action 
    
    def forward(self, x):
        x = torch.relu(self.layer1(x)) # apply ReLU function to outputs of first layer 
        x = torch.relu(self.layer2(x)) # apply ReLU function to outputs of second layer 
        return self.layer3(x) # returns Q-values for each action 