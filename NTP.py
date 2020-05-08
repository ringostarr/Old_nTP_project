import Core
import TSI
import API
import TaskSeqGen
import torch
#TSI.trainALLTasks()
state = torch.zeros(4,4)
state[0,0]=1
i = torch.zeros(6)
i[0]=1
count=0

def RUN(i,spec,state,r=0):
    fail=0
    r=0
    failure = 0
    while r<0.7:
        if fail>10:
            return
        i_next,r = Core.Predict(i,torch.flatten(spec),torch.flatten(state))
        spec_next = TSI.GetSpecFromLabel(TSI.Predict(spec,state,i))
        #iter+=1
        #count=count+1# i_next = MUTW , r =0
        #spec_next = getpaddedSpec(spec)               # i = MUTW ,r =0  i_next = moveup , r=0

        if i_next[2]>0.5 and fail<10: #MU
          #try:
              state=API.moveup(state)
              if state[2,0]==1 and i[1]==1 and failure==0:
                  print("Human Failure,placing agent at 1,0\n")
                  state = API.movedown(state)
                  failure=1
                  state[1, 0] = 1
         # except:
             # print("failure here")
             # fail=fail+1
        elif i_next[4]>0.5:  # MU
            try:
                state = API.moveright(state)
            except:
                print("failure here")
                fail = fail + 1
        else:
            print("\nCalling Heirarchical Function:",i_next)
            RUN(torch.round(i_next),spec_next,state)
            fail=fail+1

print("-------------Training complete------------------------------------- \n")
#TSI.trainALLTasks()
print("-------------------------------------------------- \n")
print("Running Move to Goal from initial position (0,0) \n")
RUN(i,TaskSeqGen.generateTaskTargetSeq(),state)
print("-------------------------------------------------- \n")
print("Running Move  upto wall from initial position (0,0) \n")



state = torch.zeros(4,4)
state[0,0]=1
i = torch.zeros(6)
i[1]=1
count=0
print("-------------------------------------------------- \n")
print("Running Move  upto wall from initial position (0,0) \n")
RUN(i,TaskSeqGen.generateTaskTargetSeq(),state)
print("-------------------------------------------------- \n")

state = torch.zeros(4,4)
state[1,0]=1
i = torch.zeros(6)
i[1]=1
count=0
print("-------------------------------------------------- \n")
print("Running Move  upto wall from initial position (1,0) \n")
RUN(i,TaskSeqGen.generateTaskTargetSeq(),state)
print("-------------------------------------------------- \n")


state = torch.zeros(4,4)
state[3,0]=1
i = torch.zeros(6)
i[0]=1
count=0
print("-------------------------------------------------- \n")
print("Running Move to goal from initial position (3,0) \n")
RUN(i,TaskSeqGen.generateTaskTargetSeq(),state)
print("-------------------------------------------------- \n")
