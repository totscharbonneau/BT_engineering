from dataclasses import dataclass

# Machine à état secondaire exécutée dans un contexte de suivi de ligne.
# Les différents états sont représentés en tant que classes.
# Les changements d'états sont regis dans la fonction doStateAction
# La condition relative au changements d'états est contenue dans les classes des états.
# Cette condition est le résultat de la lecture du changement de ligne.

with open("control/line_follower_actions.py") as f:
    code = f.read()
    exec(code)

@dataclass
class RightAhead:
    lineFollowerData: [int, int, int, int, int]

@dataclass
class VeryWeakLeft:
    lineFollowerData: [int, int, int, int, int]

@dataclass
class WeakLeft:
    lineFollowerData: [int, int, int, int, int]

@dataclass
class Left:
    lineFollowerData: [int, int, int, int, int]

@dataclass
class StrongLeft:
    lineFollowerData: [int, int, int, int, int]

@dataclass
class VeryStrongLeft:
    lineFollowerData: [int, int, int, int, int]

@dataclass
class VeryWeakRight:
    lineFollowerData: [int, int, int, int, int]

@dataclass
class WeakRight:
    lineFollowerData: [int, int, int, int, int]

@dataclass
class Right:
    lineFollowerData: [int, int, int, int, int]

@dataclass
class StrongRight:
    lineFollowerData: [int, int, int, int, int]

@dataclass
class VeryStrongRight:
    lineFollowerData: [int, int, int, int, int]

@dataclass
class HardRight:
    lineFollowerData: [int, int, int, int, int]

@dataclass
class lostLeft:
    lineFollowerData: [int, int, int, int, int]

EXIT = None

LineFollowerState = RightAhead | VeryWeakLeft | WeakLeft | Left | StrongLeft | VeryStrongLeft | VeryWeakRight | WeakRight | Right | StrongRight | VeryStrongRight | HardRight

def lineFollowerCommonChoice(self, lineFollowerData):
    if(lineFollowerData == ([0,0,1,0,0])):
        nextLineFollowerData = LineFollowerActions.RightAhead(self)
        return RightAhead(nextLineFollowerData)
    elif(lineFollowerData == [0,1,1,0,0]):
        nextLineFollowerData = LineFollowerActions.VeryWeakLeft(self)
        return VeryWeakLeft(nextLineFollowerData)
    elif(lineFollowerData == [0,1,0,0,0]):
        nextLineFollowerData = LineFollowerActions.WeakLeft(self)
        return WeakLeft(nextLineFollowerData)
    elif(lineFollowerData == [1,1,0,0,0]):
        nextLineFollowerData = LineFollowerActions.Left(self)
        return Left(nextLineFollowerData)
    elif(lineFollowerData == [1,0,0,0,0]):
        nextLineFollowerData = LineFollowerActions.StrongLeft(self)
        return StrongLeft(nextLineFollowerData)
    elif(lineFollowerData == [1,1,1,0,0]):
        nextLineFollowerData = LineFollowerActions.VeryStrongLeft(self)
        return VeryStrongLeft(nextLineFollowerData)
    elif(lineFollowerData == [0,0,1,1,0]):
        nextLineFollowerData = LineFollowerActions.VeryWeakRight(self)
        return VeryWeakRight(nextLineFollowerData)
    elif(lineFollowerData == [0,0,0,1,0]):
        nextLineFollowerData = LineFollowerActions.WeakRight(self)
        return WeakRight(nextLineFollowerData)
    elif(lineFollowerData == [0,0,0,1,1]):
        nextLineFollowerData = LineFollowerActions.Right(self)
        return Right(nextLineFollowerData)
    elif(lineFollowerData == [0,0,0,0,1]):
        nextLineFollowerData = LineFollowerActions.StrongRight(self)
        return StrongRight(nextLineFollowerData)
    elif(lineFollowerData == [0,0,1,1,1]):
        nextLineFollowerData = LineFollowerActions.VeryStrongRight(self)
        return VeryStrongRight(nextLineFollowerData)
    return None

def doLineFollowerStateAction(self, lineFollowerState: LineFollowerState):
    match lineFollowerState:
        case RightAhead(lineFollowerData):
            nextState = lineFollowerCommonChoice(self, lineFollowerData)
            if(nextState != None):
                return nextState
            if((lineFollowerData == [0,0,0,0,0]) | (lineFollowerData == [0,1,1,1,0])):
                nextLineFollowerData = LineFollowerActions.RightAhead(self)
                return RightAhead(nextLineFollowerData)
            else:
                return EXIT
        case VeryWeakLeft(lineFollowerData):
            nextState = lineFollowerCommonChoice(self, lineFollowerData)
            if(nextState != None):
                return nextState
            if((lineFollowerData == [0,0,0,0,0]) | (lineFollowerData == [0,1,1,1,0])):
                nextLineFollowerData = LineFollowerActions.WeakLeft(self)
                return WeakLeft(nextLineFollowerData)
            else:
                return EXIT
        case WeakLeft(lineFollowerData):
            nextState = lineFollowerCommonChoice(self, lineFollowerData)
            if(nextState != None):
                return nextState
            if((lineFollowerData == [0,0,0,0,0]) | (lineFollowerData == [0,1,1,1,0])):
                nextLineFollowerData = LineFollowerActions.Left(self)
                return Left(nextLineFollowerData)
            else:
                return EXIT
        case Left(lineFollowerData):
            nextState = lineFollowerCommonChoice(self, lineFollowerData)
            if(nextState != None):
                return nextState
            if((lineFollowerData == [0,0,0,0,0]) | (lineFollowerData == [0,1,1,1,0])):
                nextLineFollowerData = LineFollowerActions.StrongLeft(self)
                return StrongLeft(nextLineFollowerData)
            else:
                return EXIT
        case StrongLeft(lineFollowerData):
            nextState = lineFollowerCommonChoice(self, lineFollowerData)
            if(nextState != None):
                return nextState
            if((lineFollowerData == [0,0,0,0,0]) | (lineFollowerData == [0,1,1,1,0])):
                if self._stateActions.cycleSinceLostLine < 20:
                    self._stateActions.cycleSinceLostLine += 1
                    nextLineFollowerData = LineFollowerActions.StrongLeft(self)
                    return StrongLeft(nextLineFollowerData)
                else: 
                    self._stateActions.cycleSinceLostLine = 0
                    nextLineFollowerData = LineFollowerActions.VeryStrongLeft(self, True)
                    return VeryStrongLeft(nextLineFollowerData)
            else:
                return EXIT
        case VeryStrongLeft(lineFollowerData):
            nextLineFollowerData = LineFollowerActions.VeryStrongLeft(self)
            if nextLineFollowerData[2] == 0:
                return VeryStrongLeft(nextLineFollowerData)
            else:
                self._targetSpeed = 0
                return StrongLeft(nextLineFollowerData)
            
        case VeryWeakRight(lineFollowerData):
            nextState = lineFollowerCommonChoice(self, lineFollowerData)
            if(nextState != None):
                return nextState
            if((lineFollowerData == [0,0,0,0,0]) | (lineFollowerData == [0,1,1,1,0])):
                nextLineFollowerData = LineFollowerActions.WeakRight(self)
                return WeakRight(nextLineFollowerData)
            else:
                return EXIT
        case WeakRight(lineFollowerData):
            nextState = lineFollowerCommonChoice(self, lineFollowerData)
            if(nextState != None):
                return nextState
            if((lineFollowerData == [0,0,0,0,0]) | (lineFollowerData == [0,1,1,1,0])):
                nextLineFollowerData = LineFollowerActions.Right(self)
                return Right(nextLineFollowerData)
            else:
                return EXIT
        case Right(lineFollowerData):
            nextState = lineFollowerCommonChoice(self, lineFollowerData)
            if(nextState != None):
                return nextState
            if((lineFollowerData == [0,0,0,0,0]) | (lineFollowerData == [0,1,1,1,0])):
                nextLineFollowerData = LineFollowerActions.StrongRight(self)
                return StrongRight(nextLineFollowerData)
            else:
                return EXIT
        case StrongRight(lineFollowerData):
            nextState = lineFollowerCommonChoice(self, lineFollowerData)
            if(nextState != None):
                return nextState
            if((lineFollowerData == [0,0,0,0,0]) | (lineFollowerData == [0,1,1,1,0])):
                if self._stateActions.cycleSinceLostLine < 20:
                    self._stateActions.cycleSinceLostLine += 1
                    nextLineFollowerData = LineFollowerActions.StrongRight(self)
                    return StrongRight(nextLineFollowerData)
                else: 
                    self._stateActions.cycleSinceLostLine = 0
                    nextLineFollowerData = LineFollowerActions.VeryStrongRight(self, True)
                    return VeryStrongRight(nextLineFollowerData)
            else:
                return EXIT
        case VeryStrongRight(lineFollowerData):
            nextLineFollowerData, cycle = LineFollowerActions.VeryStrongRight(self)
            if nextLineFollowerData[2] == 0:
                return VeryStrongRight(nextLineFollowerData)
            else:
                self._targetSpeed = 0
                return StrongRight(nextLineFollowerData)
            
        case HardRight(lineFollowerData):
            nextLineFollowerData = LineFollowerActions.HardRight(self)
            if(nextLineFollowerData == [0,0,0,0,0]):
                  return HardRight(nextLineFollowerData)
            else:
                nextState = lineFollowerCommonChoice(self, nextLineFollowerData)
                if(nextState != None):
                    return nextState
                else:
                    return EXIT
