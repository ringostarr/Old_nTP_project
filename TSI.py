import torch
import torch.nn as nn
import numpy as np
import TaskSeqGen
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
# Data loader
curC,curP,curTs = TaskSeqGen.generateTSIinput()
outputs = TaskSeqGen.generateTSIoutput()
num_epochs = 1000
num_classes = 4


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1= nn.Conv1d(4,4,1)

        self.fc = nn.Linear(38,4) # num_classes
        self.smax = nn.Softmax(dim=0)
    def forward(self, x,pi,si):
        x= self.conv1(x.reshape(4,4,1))
        x=nn.functional.relu(x)
        h = torch.cat((pi.flatten(),x.flatten(),si.flatten())) # concat
        x = self.fc(h)
        x=self.smax(x)
        return x

model = Net().to(device)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.005)
import matplotlib.pyplot as plt

def train_main(inputC,inputP,inputT,outputs):

    plotloss = list()
    for i in range(1000):
        total_loss =0

        for j in range(0,8):
                #targets = data.view(-1)
            #data = data.to(device)
                #output = list()
            loss = 0
            for k in range(0,8):
                output=model(inputT[j][k],inputP[k],inputC[k])  # catastrphoic forgetting

                #print(outputs)
                #print(targetSet[j])
                #target = torch.tensor([1]).long()
                lossedge = criterion(output.view(-1),outputs[j][k])
                loss=loss+lossedge
            optimizer.zero_grad()

            loss.backward()
            optimizer.step()
            total_loss+=loss

            #if (i + 1) % 300 == 0:
                #print("Model output",output)
                #print("Label output", outputs[j][k])
        if j == 7:
            plotloss.append(total_loss)
            plt.ylabel("Loss")
            plt.plot(plotloss)
        if i %100==0:
            print('Epoch [{}/{}],Loss:{:.4f}'.format(i+1,num_epochs,total_loss))
    plt.savefig('TSILoss.png')

   # print('Epoch [{}/{}], Step [{}], Loss: {:.4f}'.format(i + 1, num_epochs, j + 1, loss.item()))

def Predict(input,curc,curp):
    TSI=list()
    for i in range(0,8):
        prediction=model.forward(input[i],curp,curc)
        TSI.append(prediction)
    return TSI
def trainALLTasks():
    #for i in range(0,8):
    print("\nTraining Task specification ")
    train_main(curC,curP,curTs,outputs)

        #m = Net().to(device)

def GetSpecFromLabel(Prediction):
    seq= torch.zeros(8, 4, 4)
    FullTS = TaskSeqGen.generateTaskTargetSeq()
    for i in range(0,8):
        if Prediction[i][1]>0.5 or Prediction[i][2]>0.5 or Prediction[i][0]>0.5:
            seq[i]= FullTS[i]
    return seq



trainALLTasks()
pytorch_total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)

print("Trainable parameters:",pytorch_total_params)
#k = Predict(curTs[0], curC[0], curP[0])
#print(k)