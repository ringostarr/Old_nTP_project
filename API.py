import torch

initx=0
inity=0
def moveuptowall(state):
    for i in range(0,4):
        state=moveup(state)
        print("calling moveuptowall")
    return state


def moverighttowall(state):
    for i in range(0,4):
        state=moveright(state)
    return state

def moveleftttowall(state):
    for i in range(0,4):
        state=movedown(state)
    return state

def movedowntowall(state):
    for i in range(0,4):
        state=movedown(state)
    return state


def moveup(state):
    print("moving up")
    x = (state==1).nonzero()
    xpos=x[0][0]
    ypos=x[0][1]
    state[xpos,ypos]=0
    state[xpos+1,ypos]=1
    return state

def movedown(state):
    #print("moving up")
    x = (state == 1).nonzero()
    xpos = x[0][0]
    ypos = x[0][1]
    state[xpos, ypos] = 0
    state[xpos -1, ypos] = 1
    return state
    return state

def moveleft(state):
    return state

def moveright(state):
    print("moving right")
    x = (state == 1).nonzero()
    xpos = x[0][0]
    ypos = x[0][1]
    state[xpos, ypos] = 0
    state[xpos , ypos+1] = 1
    return state
    #return state

def MovetoGoal(state):
    state=moveuptowall(state)
    state = moverighttowall(state)
    return state



