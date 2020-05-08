import torch
import torch.nn as nn
import TaskSeqGen
import numpy as np
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
# Data loader

num_epochs = 500
num_classes = 4

#phi_i = torch.rand(12,4,4)
targetprogram,EOPseq,CurrentProg = TaskSeqGen.generatePrgmStk()
TaskSeq = TaskSeqGen.generateTaskTargetSeq()

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()


        self.fc1 = nn.Linear(6,128)       # 6x1
        self.fc2 = nn.Linear(128,128)       # 12x4x4
        self.fc3 = nn.Linear(16, 128)      #
        self.fc4 = nn.Linear(128,6)
        self.fc5 = nn.Linear(128,1)
        self.smax = nn.Softmax(dim=0)
        self.sig = nn.Sigmoid()
    def forward(self, x1,x2,x3):

        h1 = self.fc1(x1)
        h2=self.fc2(x2)
        h3=self.fc3(x3)
        h=h1+h2+h3
        n_fc4= self.fc4(h)

        n_fc4 = self.smax(n_fc4)
        r_fc5 = self.fc5(h)

        r_fc5 = self.sig(r_fc5)

        return n_fc4,r_fc5

model1 = Net().to(device)

criterion = nn.MSELoss()

optimizer1 = torch.optim.Adam(model1.parameters(), lr=0.01)
def Predict(i,spec,state):
    i2,r=model1.forward(i,spec,state)
    return i2,r
import matplotlib.pyplot as plt
plotloss=list()
from torch.autograd import Variable
print("\nStarting Core training\n")
for i in range(500):
    total_loss1 =0
    total_loss2 = 0

    for j in range(0,8):


        #targets = data.view(-1)
        #data = data.to(device)
        #targetprogram = targetprogram.to(device)
       # k=torch.unsqueeze(TaskSeq,0)
        outputs,outputs2=model1(CurrentProg[j],torch.flatten(TaskSeq),torch.flatten(TaskSeq[j]))

        #print(outputs)
        #print(targetSet[j])
        #target = torch.tensor([1]).long()
        loss = criterion(outputs.view(-1),targetprogram[j].view(-1))
        loss2 = criterion(outputs2, EOPseq[j])
        optimizer1.zero_grad()
        loss = loss+loss2
        loss.backward()
        #loss2.backward()
        optimizer1.step()

        if j==7:
            plotloss.append(loss)
            plt.ylabel("Loss")
            plt.plot(plotloss)

            #plt.
        #total_loss1+=loss2
        #if (i + 1) % 50==0:
            #print("TimeStep:",j,outputs,outputs2)

    total_loss1 += loss
    print('Epoch [{}/{}],Loss:{:.4f}'.format(i+1,num_epochs,total_loss1))
   # print('Epoch [{}/{}], Step [{}], Loss: {:.4f}'.format(i + 1, num_epochs, j + 1, loss.item()))
plt.savefig('CoreOutput.png')
plt.close()
pytorch_total_params = sum(p.numel() for p in model1.parameters() if p.requires_grad)

print("Trainable parameters:",pytorch_total_params)

