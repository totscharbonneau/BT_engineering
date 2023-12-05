from dataclasses import dataclass
from control.mouvement_control import *
with open("control/state_actions.py") as f:
    code = f.read()
    exec(code)

@dataclass
class FollowLine:
    obstacle: bool
    finalT: bool

@dataclass
class Stop:
    stopped: bool

@dataclass
class Backward:
    done: bool

@dataclass
class GoAround:
    done: bool

@dataclass
class TStop:
    stopped: bool
    isTest: bool

@dataclass
class FinalBackward:
    done: bool

@dataclass
class FinalStop:
    stopped: bool

State = FollowLine | Stop | Backward | GoAround | TStop | FinalBackward | FinalStop

EXIT = None

class StateMachine:
    _api = None
    _stateMachine = None
    _targetAngle = 90
    _targetSpeed = 0
    _lastAngle = 90 
    _lastSpeed = 0
    _forward = False
    _backward = False

    def __init__(self, api):
        self._api = api
        self._stateActions = StateActions()
        self.mouvementControl = MouvementControl()
    
    def doStateAction(self, state : State):
        match state:
            case FollowLine(obstacle, finalT):
                match (obstacle, finalT):
                    case (False, False):
                        nextObstacle, nextFinalT = StateActions.lineFollowerAction(self)
                        return FollowLine(nextObstacle, nextFinalT)
                    case (True, False):
                        nextStopped = StateActions.stopAction(self)
                        return Stop(nextStopped)
                    case ((True | False), True):
                        nextStopped, nextIsTest = StateActions.tStop(self)
                        return TStop(nextStopped, nextIsTest)
            case Stop(stopped):
                match stopped:
                    case False:
                        nextStopped = StateActions.stopAction(self)
                        return Stop(nextStopped)
                    case True:
                        nextDone = StateActions.backwardAction(self)
                        return Backward(nextDone)
            case Backward(done):
                match done:
                    case False:
                        nextDone = StateActions.backwardAction(self)
                        return Backward(nextDone)
                    case True:
                        nextDone = StateActions.goAroundAction(self)
                        return GoAround(nextDone)
            case GoAround(done):
                match done:
                    case False:
                        nextDone = StateActions.goAroundAction(self)
                        return GoAround(nextDone)
                    case True:
                        nextObstacle, nextFinalT = StateActions.lineFollowerAction(self)
                        return FollowLine(nextObstacle, nextFinalT)
            case TStop(stopped, isTest):
                match (stopped, isTest):
                    case (False, (True | False)):
                        nextStopped, nextIsTest = StateActions.tStop(self)
                        return TStop(nextStopped, nextIsTest)
                    case (True, False):
                        return EXIT
                    case (True, True):
                        nextDone = StateActions.finalBackward(self)
                        return FinalBackward(nextDone)
            case FinalBackward(done):
                match (done):
                    case False:
                        nextDone = StateActions.finalBackward(self)
                        return FinalBackward(nextDone)
                    case True:
                        nextStopped = StateActions.finalStop(self)
                        return FinalStop(nextStopped)
            case FinalStop(stopped):
                match stopped:
                    case False:
                        nextStopped = StateActions.finalStop(self)
                        return FinalStop(nextStopped)
                    case True:
                        return EXIT

    def loopStateMachine(self):
        stateobj = FollowLine(False, False)
        for i in range(NUMBEROFCYCLES):
            print([i, stateobj])
            stateobj = StateMachine.doStateAction(self=self, state=stateobj)
            if(stateobj == EXIT):
                self._targetAngle = 90
                self._targetSpeed = 0
            self.adjustAngle()
            self.adjustSpeed()
            # self._api.move()
            self._api.cycleAction(i)
        self._api.backWheels.speed = 0
    
    def adjustAngle(self):
        self._api.frontWheels.turn(int(self.mouvementControl.ajusterAngle(self._targetAngle)))
        """if(self._targetAngle > self._lastAngle+20):
            self._lastAngle += 15
            self._api.frontWheels.turn(self._lastAngle)
        elif(self._targetAngle < self._lastAngle-20):
            self._lastAngle -= 15
            self._api.frontWheels.turn(self._lastAngle)
        else:
            self._api.frontWheels.turn(self._targetAngle)"""

    def adjustSpeed(self):
        if self._api.backWheels.speed < 0:
            self._api.backWheels.backward()
        else:
            self._api.backWheels.forward()
        self._api.backWheels.speed = int(self.mouvementControl.ajusterVitesse(self._targetSpeed))
        """if(self._targetSpeed > self._lastSpeed):
        if(self._forward & self._backward):
            self._targetSpeed = 15
            if(self._lastSpeed <= 15):
                self._forward = False
                self._backward = False
        elif(self._forward and not self._backward):
            self._api.backWheels.forward()
        elif(not self._forward and self._backward):
            self._api.backWheels.backward()
        if(self._targetSpeed > self._lastSpeed):
            self._lastSpeed += 3
            self._api.backWheels.speed = self._lastSpeed
        elif(self._targetSpeed < self._lastSpeed):
            self._lastSpeed -= 3
            self._api.backWheels.speed = self._lastSpeed"""