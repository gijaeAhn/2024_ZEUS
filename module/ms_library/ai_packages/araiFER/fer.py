import torch
from torch import nn

def conv_block(in_channels, out_channels, pool=False):
    layers = [nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1), 
              nn.BatchNorm2d(out_channels), 
              nn.ReLU(inplace=True)]
    if pool: layers.append(nn.MaxPool2d(2))
    return nn.Sequential(*layers)


class ARAIFER(nn.Module):
    def __init__(self, attribute_num):
        super().__init__()
        #feature extraction layer 
        self.input = conv_block(1, 64)

        self.conv1 = conv_block(64, 64, pool=True)
        self.res1 = nn.Sequential(conv_block(64, 32), conv_block(32, 64))
        self.drop1 = nn.Dropout(0.3)
        
        self.conv2 = conv_block(64, 64, pool=True)
        self.res2 = nn.Sequential(conv_block(64, 32), conv_block(32, 64))
        self.drop2 = nn.Dropout(0.3)
        
        self.conv3 = conv_block(64, 64, pool=True)
        self.res3 = nn.Sequential(conv_block(64, 32), conv_block(32, 64))
        self.drop3 = nn.Dropout(0.3)

        self.conv4 = conv_block(64,64, pool=False)
        self.res4 = nn.Sequential(conv_block(64, 32), conv_block(32, 64))
        self.drop4 = nn.Dropout(0.3)
        
        self.classifier = nn.Sequential(nn.MaxPool2d(6), 
                                        nn.Flatten(),
                                        nn.Linear(64, 64),
                                        nn.Dropout(0.3),
                                        nn.BatchNorm1d(64),
                                        nn.PReLU(),
                                        nn.Linear(64, 64),
                                        nn.Dropout(0.3),
                                        nn.BatchNorm1d(64),
                                        nn.PReLU(),
                                        nn.Linear(64, 64),
                                        nn.Dropout(0.3),
                                        nn.BatchNorm1d(64),
                                        nn.PReLU(),
                                        nn.Linear(64, 1),
                                        )
        self.last_layer = nn.Sigmoid()
    

    def forward(self, x):
        out = self.input(x)

        out = self.conv1(out)
        out = self.res1(out) + out
        out = self.drop1(out)
        
        out = self.conv2(out)
        out = self.res2(out) + out
        out = self.drop2(out)
        
        out = self.conv3(out)
        out = self.res3(out) + out
        out = self.drop3(out)

        out = self.conv4(out)
        out = self.res4(out) + out
        out = self.drop4(out)

        
        out = self.classifier(out)
        return self.last_layer(out)
    
   
    

if __name__ == "__main__":
    a = torch.rand([7,1,48,48])
    model = ARAIFER(3)

    b = model(a)
    print(b.size())