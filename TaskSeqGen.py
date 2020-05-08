import numpy as np
import API
import torch


def generateTaskTargetSeq():
    targetSet = torch.zeros(8, 4, 4) #t,s
    targetSet[0, 0, 0] = 1
    targetSet[1, 0, 0] = 1
    targetSet[2, 1, 0] = 1
    targetSet[3, 2, 0] = 1
    targetSet[4, 3, 0] = 1
    targetSet[5, 3, 0] = 1
    targetSet[6, 3, 1] = 1
    targetSet[7, 3, 2] = 1
    #targetSet[7, 3, 3] = 1
    #targetSet[9, 3, 2] = 1
    #targetSet[10, 3, 3] = 1
    #targetSet[11, 3, 3] = 1
    #targetSet[12, 3, 3] = 1
    return targetSet

def generatePrgmStk():
    targetProgram = torch.zeros(8,6)
    CurrentProgram = torch.zeros(8, 6)
    #targetProgram[0,0]  =1              #10000 -> Movetogoal
    targetProgram[0, 1] =1              #01000 -> Moveuptowall                        movetogoal
    targetProgram[1, 2] =1              #00100  -> Moveup
    targetProgram[2, 2] =1              #00100  -> Moveup
    targetProgram[3, 2] =1              #00100  -> Moveup
    targetProgram[4,3] = 1              #moveuptowall ends here
   #targetProgram[5,0] = 1              #recursion back to move to goal
    targetProgram[5, 4] =1              #00010  -> Moverightowall
    targetProgram[6, 4] = 1             #00001  -> Moveright
    targetProgram[7, 4] = 1             #00001  -> Moveright
   # targetProgram[8, 4] = 1             #00001  -> Moveright
    #targetProgram[9,3] = 1              #moveright ends here
   # targetProgram[10, 0] = 1              # movetogoal ends
    #targetProgram[11,5] =1

#mtg -> (moveuptow and moveright)
#
    CurrentProgram[0, 0] = 1
    CurrentProgram[1, 1] = 1
    CurrentProgram[2, 1] = 1
    CurrentProgram[3, 1] = 1
    CurrentProgram[4, 0] = 1
    #CurrentProgram[5, 0] = 1
    CurrentProgram[5, 3] = 1
    CurrentProgram[6, 3] = 1
    CurrentProgram[7, 3] = 1
    #CurrentProgram[8, 3] = 1
    #CurrentProgram[10, 0] = 1
    #CurrentProgram[11, 0] = 1

    EOP = torch.zeros(8,1)
    #EOP[1]=1       #01000 r>alpha
    #EOP[2] = 1     # 1->MYTW->MOVEUP'S R = 1
    #EOP[3] =1
    EOP[3] = 1  # 01000 r>alpha
    EOP[4] = 1
    #EOP[6] = 1
    #EOP[7] = 1
    #EOP[8] = 1  # 01000 r>alpha
    EOP[7] = 1
    #EOP[11] = 1
    return targetProgram,EOP,CurrentProgram


def uptowallTaskseq():
    targetSet = torch.zeros(8, 4, 4)  # t,s
    targetSet = torch.zeros(8, 4, 4)  # t,s
    #targetSet[0, 0, 0] = 1
    targetSet[1, 0, 0] = 1
    targetSet[2, 1, 0] = 1
    targetSet[3, 2, 0] = 1
    targetSet[4, 3, 0] = 1
    #targetSet[5, 3, 0] = 1
    #targetSet[6, 3, 1] = 1
    #targetSet[7, 3, 2] = 1

    return targetSet
def upTaskspec1():
    targetSet = torch.zeros(8, 4, 4)  # t,s
    targetSet = torch.zeros(8, 4, 4)  # t,s
    #targetSet[0, 0, 0] = 1
    targetSet[1, 0, 0] = 1
    targetSet[2, 1, 0] = 1
    #targetSet[3, 2, 0] = 1
    #targetSet[4, 3, 0] = 1
    #targetSet[5, 3, 0] = 1
    #targetSet[6, 3, 1] = 1
    #targetSet[7, 3, 2] = 1

    return targetSet
def upTaskspec2():
    targetSet = torch.zeros(8, 4, 4)  # t,s
    targetSet = torch.zeros(8, 4, 4)  # t,s
    #targetSet[0, 0, 0] = 1
    #targetSet[1, 0, 0] = 1
    targetSet[2, 1, 0] = 1
    targetSet[3, 2, 0] = 1
    #targetSet[4, 3, 0] = 1
    #targetSet[5, 3, 0] = 1
    #targetSet[6, 3, 1] = 1
    #targetSet[7, 3, 2] = 1

    return targetSet
def upTaskspec3():
    targetSet = torch.zeros(8, 4, 4)  # t,s
    targetSet = torch.zeros(8, 4, 4)  # t,s
    #targetSet[0, 0, 0] = 1
    #targetSet[1, 0, 0] = 1
    #targetSet[2, 1, 0] = 1
    targetSet[3, 2, 0] = 1
    #targetSet[4, 3, 0] = 1
    #targetSet[5, 3, 0] = 1
    #targetSet[6, 3, 1] = 1
    #targetSet[7, 3, 2] = 1

    return targetSet
def righttowallTaskseq():
    targetSet = torch.zeros(8, 4, 4)  # t,s
    #targetSet[0, 0, 0] = 1
    #targetSet[1, 0, 0] = 1
    #targetSet[2, 0, 0] = 1
    #targetSet[3, 1, 0] = 1
    #targetSet[4, 2, 0] = 1
    targetSet[5, 3, 0] = 1
    targetSet[6, 3, 1] = 1
    targetSet[7, 3, 2] = 1
    #targetSet[8, 3, 3] = 1
    # targetSet[9, 3, 3] = 1

    return targetSet
def rightTaskseq1():
    targetSet = torch.zeros(8, 4, 4)  # t,s
    #targetSet[0, 0, 0] = 1
    #targetSet[1, 0, 0] = 1
    #targetSet[2, 0, 0] = 1
    #targetSet[3, 1, 0] = 1
    #targetSet[4, 2, 0] = 1
    targetSet[5, 3, 0] = 1
    targetSet[6, 3, 1] = 1
    #targetSet[7, 3, 2] = 1
    #targetSet[8, 3, 3] = 1
    # targetSet[9, 3, 3] = 1

    return targetSet
def rightTaskseq2():
    targetSet = torch.zeros(8, 4, 4)  # t,s
    #targetSet[0, 0, 0] = 1
    #targetSet[1, 0, 0] = 1
    #targetSet[2, 0, 0] = 1
    #targetSet[3, 1, 0] = 1
    #targetSet[4, 2, 0] = 1
    #targetSet[5, 3, 0] = 1
    targetSet[6, 3, 1] = 1
    targetSet[7, 3, 2] = 1
    #targetSet[8, 3, 3] = 1
    # targetSet[9, 3, 3] = 1

    return targetSet
def rightTaskseq3():
    targetSet = torch.zeros(8, 4, 4)  # t,s
    #targetSet[0, 0, 0] = 1
    #targetSet[1, 0, 0] = 1
    #targetSet[2, 0, 0] = 1
    #targetSet[3, 1, 0] = 1
    #targetSet[4, 2, 0] = 1
    #targetSet[5, 3, 0] = 1
    targetSet[6, 3, 1] = 1
    targetSet[7, 3, 2] = 1
    #targetSet[8, 3, 3] = 1
    # targetSet[9, 3, 3] = 1

    return targetSet
def uptowallTSI():
    targetSet = torch.zeros(8, 4)  # t,s
    targetSet[0, 3] = 1
    targetSet[1, 0] = 1
    targetSet[2, 2] = 1
    targetSet[3, 2] = 1
    targetSet[4, 1] = 1
    targetSet[5, 3] = 1
    targetSet[6, 3] = 1
    targetSet[7, 3] = 1
    #targetSet[8, 3] = 1

    return targetSet
def upTSI1():
    targetSet = torch.zeros(8, 4)  # t,s
    targetSet[0, 3] = 1
    targetSet[1, 0] = 1
    targetSet[2, 1] = 1
    targetSet[3, 3] = 1
    targetSet[4, 3] = 1
    targetSet[5, 3] = 1
    targetSet[6, 3] = 1
    targetSet[7, 3] = 1
    #targetSet[8, 3] = 1

    return targetSet
def upTSI2():
    targetSet = torch.zeros(8, 4)  # t,s
    targetSet[0, 3] = 1
    targetSet[1, 3] = 1
    targetSet[2, 0] = 1
    targetSet[3, 1] = 1
    targetSet[4, 3] = 1
    targetSet[5, 3] = 1
    targetSet[6, 3] = 1
    targetSet[7, 3] = 1
    #targetSet[8, 3] = 1

    return targetSet
def upTSI3():
    targetSet = torch.zeros(8, 4)  # t,s
    targetSet[0, 3] = 1
    targetSet[1, 3] = 1
    targetSet[2, 3] = 1
    targetSet[3, 0] = 1
    targetSet[4, 1] = 1
    targetSet[5, 3] = 1
    targetSet[6, 3] = 1
    targetSet[7, 3] = 1
    #targetSet[8, 3] = 1

    return targetSet
def righttowallTSI():
    targetSet = torch.zeros(8, 4)  # t,s
    targetSet[0, 3] = 1
    targetSet[1, 3] = 1
    targetSet[2, 3] = 1
    targetSet[3, 3] = 1
    targetSet[4, 0] = 1
    targetSet[5, 2] = 1
    targetSet[6, 2] = 1
    targetSet[7, 1] = 1
    #targetSet[8, 1] = 1
    # targetSet[9, 3, 3] = 1
    return targetSet
# 8x
def rightTSI1():
    targetSet = torch.zeros(8, 4)  # t,s
    targetSet[0, 3] = 1
    targetSet[1, 3] = 1
    targetSet[2, 3] = 1
    targetSet[3, 3] = 1
    targetSet[4, 3] = 1
    targetSet[5, 0] = 1
    targetSet[6, 1] = 1
    targetSet[7, 3] = 1
    #targetSet[8, 3] = 1

    return targetSet
def rightTSI2():
    targetSet = torch.zeros(8, 4)  # t,s
    targetSet[0, 3] = 1
    targetSet[1, 3] = 1
    targetSet[2, 3] = 1
    targetSet[3, 3] = 1
    targetSet[4, 3] = 1
    targetSet[5, 3] = 1
    targetSet[6, 0] = 1
    targetSet[7, 1] = 1
    #targetSet[8, 3] = 1

    return targetSet
def rightTSI3():
    targetSet = torch.zeros(8, 4)  # t,s
    targetSet[0, 3] = 1
    targetSet[1, 3] = 1
    targetSet[2, 3] = 1
    targetSet[3, 3] = 1
    targetSet[4, 3] = 1
    targetSet[5, 3] = 1
    targetSet[6, 0] = 1
    targetSet[7, 1] = 1
    #targetSet[8, 3] = 1

    return targetSet




def generateTSIinput():
    Cp = torch.zeros(6)
    Cs = torch.zeros(4,4)
    Ts = torch.zeros(8,4,4)
    #input=list()
    Cp[0]=1
    Cs[0,0]=1
    Ts = generateTaskTargetSeq()
    inputCp=list()
    inputCs=list()
    inputTs=list()
    inputCp.append(Cp)
    inputCs.append(Cs)
    inputTs.append(Ts)

    Cp = torch.zeros(6)
    Cs = torch.zeros(4, 4)
    Ts = torch.zeros(8, 4, 4)
    Cp[1]=1
    Cs[0,0]=1
    Ts = upTaskspec1()
    inputCp.append(Cp)
    inputCs.append(Cs)
    inputTs.append(Ts)

    Cp = torch.zeros(6)
    Cs = torch.zeros(4, 4)
    Ts = torch.zeros(8, 4, 4)
    Cp[1] = 1
    Cs[1, 0] = 1
    Ts = upTaskspec2()
    inputCp.append(Cp)
    inputCs.append(Cs)
    inputTs.append(Ts)

    Cp = torch.zeros(6)
    Cs = torch.zeros(4, 4)
    Ts = torch.zeros(8, 4, 4)
    Cp[1] = 1
    Cs[2, 0] = 1
    Ts = upTaskspec3()
    inputCp.append(Cp)
    inputCs.append(Cs)
    inputTs.append(Ts)

    Cp = torch.zeros(6)
    Cs = torch.zeros(4, 4)
    Ts = torch.zeros(8, 4, 4)
    Cp[0] = 1
    Cs[3, 0] = 1
    Ts = righttowallTaskseq()
    inputCp.append(Cp)
    inputCs.append(Cs)
    inputTs.append(Ts)

    Cp = torch.zeros(6)
    Cs = torch.zeros(4, 4)
    Ts = torch.zeros(8, 4, 4)
    Cp[3] = 1
    Cs[3, 0] = 1
    Ts = rightTaskseq1()
    inputCp.append(Cp)
    inputCs.append(Cs)
    inputTs.append(Ts)

    Cp = torch.zeros(6)
    Cs = torch.zeros(4, 4)
    Ts = torch.zeros(8, 4, 4)
    Cp[3] = 1
    Cs[3, 1] = 1
    Ts = rightTaskseq2()
    inputCp.append(Cp)
    inputCs.append(Cs)
    inputTs.append(Ts)

    Cp = torch.zeros(6)
    Cs = torch.zeros(4, 4)
    Ts = torch.zeros(8, 4, 4)
    Cp[3] = 1
    Cs[3, 2] = 1
    Ts = rightTaskseq3()
    inputCp.append(Cp)
    inputCs.append(Cs)
    inputTs.append(Ts)

    return inputCs,inputCp,inputTs


def generateTSIoutput():
    outputTs = list()
    outputTs.append(uptowallTSI())
    outputTs.append(upTSI1())
    outputTs.append(upTSI2())
    outputTs.append(upTSI3())
    outputTs.append(righttowallTSI())
    outputTs.append(rightTSI1())
    outputTs.append(rightTSI2())
    outputTs.append(rightTSI3())

    return outputTs